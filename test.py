#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:FCQ
# datetime:2018/4/22 14:41
# software: PyCharm

#本代码从列表获取数据

import matplotlib.pyplot as plt
import numpy as np

def get_a(x):
    a = 0.0
    for i in x:
        a = a + (i * i)
    return a

def get_b(x):
    a = 0.0
    for i in x:
        a = a + i
    return a

def get_c(x, y):
    a = 0.0
    for i in range(len(x)):
        a = a + x[i] * y[i]
    return a

def get_d(y):
    a = 0.0
    for i in y:
        a = a + i
    return a

def print_list(ilist):
    '打印数据，没啥用'
    for i in ilist:
        print(i, ",", end="")
    print("\n")

plt.figure()#使用plt.figure定义一个图像窗口
plt.title('single variable')#图像标题
plt.xlabel('x')#x轴标题
plt.ylabel('y')#y轴标题
#数据组
listx = [1430, 2950, 1710, 2320, 1090, 2620, 4220, 2250]
listy = [310000, 650000, 233000, 580500, 535000, 605000, 775000, 292500]

plt.grid(True)#是否打开网格
# generate 20 points in 0~5500 randomly
x = np.linspace(0, 5500, 8)#线性回归方程线
#while(1):
plt.clf()#点重叠

#等式计算
A = get_a(listx)
B = get_b(listx)
C = get_c(listx, listy)
D = get_d(listy)
n = len(listx)
a = (B*D-C*n)/(B*B-n*A)
b = (B*C-D*A)/(B*B-n*A)
print_list(listx)
print_list(listy)
plt.scatter(listx, listy)#描点
plt.plot(x, a * x + b, 'g-')#绘制线条

#线性回归方程
a = "%.4f" % a
b = "%.4f" % b
print('y'+'='+a+'*x'+'+'+b)
plt.pause(1)#画图延时

#预测环节
x = input("请输入x,预测y-->>")
x = int(x)
y = float(a) * x + float(b)
print('y', '=', y)

