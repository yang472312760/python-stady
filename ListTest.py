#! /usr/bin/python3
# Author:yang
# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 14:59
# @Author: yang
# @Site: 
# @File: ListTest
# @Software: PyCharm
list = ['abcd', 786, 2.23, 'runoob', 70.2]

print(list[1:3])
# [786, 2.23]
tinylist = [123, 'runoob']
# ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
print(list + tinylist)

nameList = ['xiaozhang', 'xiaowang', 'xiaohua']

print(nameList[0])
print(nameList[1])
print(nameList[2])

for name in nameList:
    print(name)