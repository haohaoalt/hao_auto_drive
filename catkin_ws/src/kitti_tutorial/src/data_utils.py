#! /usr/bin/python
'''
Author: zhanghao
Date: 2022-12-01 18:19:49
LastEditTime: 2022-12-01 21:26:44
FilePath: /hao_auto_drive/catkin_ws/src/kitti_tutorial/src/data_utils.py
Description: 
'''
IMU_COLUMN_NAMES=['lat','lon','alt',
'roll','pitch','yaw',
'vn','ve','vf','vl','vu',
'ax','ay','az','af','al','au',
'wx','wy','wz','wf','wl','wu',
'posacc','velacc','navstat','numsats','posmode','velmode','orimode']

import cv2
import numpy as np
import pandas as pd
def read_camera(path):
    return cv2.imread(path)

def read_point_cloud(path):
    return np.fromfile(path, dtype=np.float32).reshape(-1,4)

def read_imu(path):
    df = pd.read_csv(path,header=None, sep=' ')
    df.columns = IMU_COLUMN_NAMES
    return df