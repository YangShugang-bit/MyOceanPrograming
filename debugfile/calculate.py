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
import re
import linecache
import pandas as pd
import sys
import os

#
# fileDir = "D:/2019工作项目/201909温州洞头大小门岛/sontek/GPS_MODEL_SpringTide083113-083121"
# for root, dirs, files in os.walk(fileDir):
#     for dir in dirs:
#         print(os.path.join(root, dir))
#     for file in files:
#         print(os.path.join(root, file))  # 文件路径
#         name,suffix = os.path.splitext(file)  #文件名、后缀名
def loaddata(filename):
    # Try to read a txt file and return a matrix.Return [] if there was a mistake.
    try:
        file = open(filename, 'r')
    except IOError:
        error = []
        return error
    content = file.readlines()
    print(content)
    rows = len(content)  # 文件行数
    print('lines = ',rows)
    datamat = np.zeros((rows, 61))  # 初始化矩阵
    row_count = 0

    for i in range(1,rows):
        content[i] = content[i].strip().split('\t')  #去空格 以制表符分隔读取
        content[i] = [float(xx) for xx in content[i]]
        datamat[row_count, :] = content[i][:]
        row_count += 1

    file.close()
    return datamat


if __name__ == '__main__':
    fileDir = "D:/2019工作项目/201909温州洞头大小门岛/sontek/GPS_MODEL_SpringTide083113-083121/083120/WENZH1908311958.spd"
    out = loaddata(fileDir)
    print(out)



