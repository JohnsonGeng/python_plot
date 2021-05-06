#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''

@File    :   main.py    
@Author  :   你牙上有辣子
@Contact :   johnsongunn23@gmail.com
@Create Time : 2021-05-06 18:17     
@Discription : 利用matplotlib对数据进行绘图，包括饼状图、柱状图、折线图等


'''

# import lib
import matplotlib.pyplot as plt
import numpy as np

name_list = ['2.15', "2.16", "2.17", "2.18", "2.19", "2,20", "2,21", "2,22", "2.23", "2.24"]
addition = [0, 0, 0, 0, 2, 0, 0, 0, 0, 1]
cancellation = [13, 34, 26, 7, 22, 1, 5, 20, 5, 25]
width = 0.3
x = list(range(len(addition)))
index = np.arange(len(name_list))

plt.figure(figsize=(8,6),dpi=500)
plt.bar(index, addition, width, color='yellowgreen', label='addition')
plt.bar(index + width, cancellation, width, color='deepskyblue', label='cancellation')
plt.legend(['addition', 'cancellation'])

bar_locs = np.arange(10)
xtick_labels = [name_list[i] for i in range(10)]
plt.xticks(bar_locs + width / 2, xtick_labels, rotation=45)
# 柱状图 X 轴标识
for a, b in zip(index, addition):  # 柱子上的数字显示
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)
for a, b in zip(index + width, cancellation):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=10)
plt.ylim(0, 40)
plt.xlabel('Date')
plt.ylabel('Number of train additions or cancellations')
plt.title('Comparison of addition and cancellation of trains')
plt.legend(loc='best')
plt.savefig("bar.png")
plt.show()