# coding = utf-8
# /usr/yangshugang/Anaconda3 python3.7

'''
Author:Yang Shugang
Email :yangshugang12@stu.ouc.edu.cn or yangshugang@theidi.com
Number:18205422083
date  :2019-10-16 09:45
introduction:uesd to
des
'''

import numpy as np
import pandas as pd
import sys
import os


# fileDir = "D:/2019工作项目/201909温州洞头大小门岛/sontek/GPS_MODEL_SpringTide083113-083121"
# for root, dirs, files in os.walk(fileDir):
#     for dir in dirs:
#         print(os.path.join(root, dir))
#     for file in files:
#         print(os.path.join(root, file))  # 文件路径
#         name,suffix = os.path.splitext(file)  #文件名、后缀名
def loaddata(filename):
    file = open(filename)
    lines = file.readlines()
    # print lines
    # ['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']形式
    rows = len(lines)  # 文件行数

    datamat = np.zeros((rows, 61))  # 初始化矩阵

    row = 0
    for line in lines:
        line = line.strip().split('\t')  # strip()默认移除字符串首尾空格或换行符
        datamat[row, :] = line[:]
        row += 1
        print(datamat)

    return datamat


    fileDir = u"D:/2019工作项目/201909温州洞头大小门岛/sontek/GPS_MODEL_SpringTide083113-083121" \
              u"/08311930/WENZH1908311930.spd"
    out = loaddata(fileDir)
    print(out)