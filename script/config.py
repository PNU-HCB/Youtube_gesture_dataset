# ------------------------------------------------------------------------------
# Copyright (c) ETRI. All rights reserved.
# Licensed under the BSD 3-Clause License.
# This file is part of Youtube-Gesture-Dataset, a sub-project of AIR(AI for Robots) project.
# You can refer to details of AIR project at https://aiforrobots.github.io
# Written by Youngwoo Yoon (youngwoo@etri.re.kr)
# ------------------------------------------------------------------------------

from datetime import datetime


class Config:
    DEVELOPER_KEY = "AIzaSyDU5_CIzz469CtI_YuQbQEmSOrZCsRlQmc"  # your youtube developer id
    OPENPOSE_BASE_DIR = 'C:\\Users\\makem\\ProjectHcb\\work\\openpose'
    OPENPOSE_BIN_PATH = 'C:\\Users\\makem\\ProjectHcb\\work\\openpose\\bin\\OpenPoseDemo.exe'


class TEDConfig(Config):
    YOUTUBE_CHANNEL_ID = "UC_pOKLycxyVwNneMVjfMBUA"
    WORK_PATH = 'C:\\Users\\makem\\ProjectHcb\\res\\Youtube_Dataset'
    CLIP_PATH = WORK_PATH + "/clip_ted"
    VIDEO_PATH = WORK_PATH + "/videos_ted"
    SKELETON_PATH = WORK_PATH + "/skeleton_ted"
    SUBTITLE_PATH = VIDEO_PATH
    OUTPUT_PATH = WORK_PATH + "/output"
    VIDEO_SEARCH_START_DATE = datetime(2022, 6, 1, 0, 0, 0)
    LANG = 'ko'
    SUBTITLE_TYPE = 'auto'
    FILTER_OPTION = {"threshold": 100}
    USE_3D_POSE = False


class LaughConfig(Config):
    YOUTUBE_CHANNEL_ID = "UCxyCzPY2pjAjrxoSYclpuLg"
    WORK_PATH = '/mnt/work/work/Youtube_Dataset'
    CLIP_PATH = WORK_PATH + "/clip_laugh"
    VIDEO_PATH = WORK_PATH + "/videos_laugh"
    SKELETON_PATH = WORK_PATH + "/skeleton_laugh"
    SUBTITLE_PATH = VIDEO_PATH
    OUTPUT_PATH = WORK_PATH + "/output"
    VIDEO_SEARCH_START_DATE = datetime(2022, 7, 20, 0, 0, 0)
    LANG = 'en'
    SUBTITLE_TYPE = 'auto'
    FILTER_OPTION = {"threshold": 50}


# SET THIS
my_config = TEDConfig