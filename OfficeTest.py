#! /usr/bin/python3
# Author:yang
# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 15:29
# @Author: yang
# @Site: 
# @File: OfficeTest
# @Software: PyCharm

import random

# 定义一个列表用来保存3个办公室
offices = [[], [], []]

# 定义一个列表用来存储8位老师的名字
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

i = 0

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d' % (i, len(tempNames)))
    i += 1
    for name in tempNames:
        print("%s" % name, end='')
    print("\n")
    print("_" * 20)
