import glob
import json
import os
import pickle
import subprocess

import shutil

from config import my_config

video_files = glob.glob(my_config.VIDEO_PATH + "/*.mp4")
sorted_video_files = sorted(video_files, key=os.path.getmtime)
sliced_video_files = sorted_video_files[328:]
for file in sliced_video_files:
    print(file)
# for i, file in enumerate(sorted_video_files, start=0):
#     print(i)
#     if "GgmhQrd3sTc" in file:
#         print("찾았다")
#         break


