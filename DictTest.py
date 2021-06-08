#! /usr/bin/python3
# Author:yang
# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 17:05
# @Author: yang
# @Site: 
# @File: DictTest
# @Software: PyCharm
info = {'name': '班长', 'id': 100, 'address': '北京'}
print(info['name'])  # 获取名字
# print(info['sex'])  # 获取不存在的key，会发生异常
print(info.get('sex'))  # 获取不存在的key，获取到空的内容，不会出现异常

age = info.get('age') #'age'键不存在，所以age为None
print(type(age)) # <type 'NoneType'>
age1 = info.get('age', 18) # 若info中不存在'age'这个键，就返回默认值18
print(age1)
