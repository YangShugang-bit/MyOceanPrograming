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

import time

def fun1():
    time.sleep(1)

def fun2():
    time.sleep(1)

def fun3():
    time.sleep(2)

def fun4():
    time.sleep(1)

def fun5():
    time.sleep(1)
    fun4()

fun1()
fun2()
fun3()
fun5()