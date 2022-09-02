import numpy as np
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras import backend as K
from tensorflow.keras import models
import datetime

class Inference():

    def __init__(self, model_json, model_weight):

        model_graph = open(model_json, 'r')
        model_loaded = model_graph.read()
        model_graph.close()

        model = model_from_json(model_loaded)
        model.load_weights(model_weight)
        model.compile(loss = self.euc_dist_keras, optimizer = 'adam')
        self.model = model

    def preprocess_skeletons(self, keypoints):
        for i in range(len(keypoints)):
            if np.isnan(keypoints[i]):
                keypoints[i] = 0

    def get_median_from_skeletons(self,skeletons):
        x_mid=[0]*15
        y_mid=[0]*15
        x=[]
        y=[]
        for i in range(15):
            x.append([0])
            y.append([0])
        for keypoints in skeletons:

            self.preprocess_skeletons(keypoints)
            key2d = []
            for i in range(0, len(keypoints), 2):
                key2d.append((keypoints[i], keypoints[i + 1]))
            keypoints = key2d
            keypoints = np.array(keypoints)
            x1 = keypoints[..., 0]
            y1 = keypoints[..., 1]

            for i in range(15):
                if(x[i]!=0 and y[i]!=0):
                    x[i].append(x1[i])
                    y[i].append(y1[i])
        for i in range(15):
            x_mid[i]=np.median(x[i])
            y_mid[i] = np.median(y[i])
        return x_mid, y_mid

    def make3D(self,skeletons):
        skeleton_3d = []
        x_mid,y_mid = self.get_median_from_skeletons(skeletons)
        for keypoints in skeletons:

            self.preprocess_skeletons(keypoints)
            model = self.model
            key2d=[]
            for i in range(0,len(keypoints),2):
                key2d.append((keypoints[i],keypoints[i+1]))
            keypoints = key2d
            x_std, y_std = [], []
            keypoints = np.array(keypoints)
            x1 = keypoints[..., 0]
            y1 = keypoints[..., 1]
            for i in range(15):
                if x1[i] == 0:
                    x1[i]=x_mid[i]
                if y1[i] == 0:
                    y1[i] = y_mid[i]

            try:
                x = [x1[8], x1[1], x1[0],
                     x1[2], x1[3], x1[4],
                     x1[5], x1[6], x1[7],
                     x1[9], x1[10], x1[11],
                     x1[12], x1[13], x1[14]]

                y = [y1[8], y1[1], y1[0],
                     y1[2], y1[3], y1[4],
                     y1[5], y1[6], y1[7],
                     y1[9], y1[10], y1[11],
                     y1[12], y1[13], y1[14]]

                xm = np.mean(x)
                ym = np.mean(y)
                sigma_x = np.std(x)
                sigma_y = np.std(y)
                for l in range(len(keypoints)):
                    xs = (x[l] - xm) / ((sigma_x + sigma_y) / 2)
                    ys = (y[l] - ym) / ((sigma_x + sigma_y) / 2)
                    x_std.append(xs)
                    y_std.append(ys)
                inpt = np.concatenate((x_std, y_std))
                inpt = inpt.reshape(1, len(inpt))
                output = model.predict(inpt)
                z = output[0]
                for k in range(len(z)):
                    z[k] = abs((z[k] * ((sigma_x + sigma_y) / 2)))

                self.swap_list(x, y, z, 0, 2)
                self.swap_list(x, y, z, 2, 3)
                self.swap_list(x, y, z, 3, 4)
                self.swap_list(x, y, z, 4, 5)
                self.swap_list(x, y, z, 5, 6)
                self.swap_list(x, y, z, 6, 7)

                #척추
                self.swap_list(x, y, z, 0, 8)
                #아래머리

                #윗머리
                self.swap_list(x, y, z, 8, 2)

                #오른쪾어깨
                self.swap_list(x, y, z, 3, 8)
                #오른쪽팔꿈치
                self.swap_list(x, y, z, 4, 8)
                #오른주먹
                self.swap_list(x, y, z, 5, 8)
                #왼쪽어깨
                self.swap_list(x, y, z, 6, 8)
                #왼쪾팔꿈치
                self.swap_list(x, y, z, 7, 8)


                result = []
                for i in range(9):
                    result.append([x[i], y[i], z[i]])
                skeleton_3d.append(result)
            except Exception as e:

                print("except: ", e)
                continue

        return skeleton_3d

    def euc_dist_keras(self, y_true, y_pred):
        return K.sqrt(K.sum(K.square(y_true - y_pred), axis=-1, keepdims=True))

    def swap_list(self, x, y, z, origin_index, switch_index):
        x[origin_index], x[switch_index] = x[switch_index], x[origin_index]
        y[origin_index], y[switch_index] = y[switch_index], y[origin_index]
        z[origin_index], z[switch_index] = z[switch_index], z[origin_index]