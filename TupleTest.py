#! /usr/bin/python3
# Author:yang
# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 16:28
# @Author: yang
# @Site: 
# @File: TupleTest
# @Software: PyCharm

t = ('abcde', 786, 2.23, 'runoob', 70.2)
t1 = (1,)
t2 = ('a', 'b', ['a', 'b'])
t2[2][0] = 'X'

print(t2)

tup1 = (50,)
print(type(tup1))

tup2 = ('google', 'baidu', 2000, 2020)
tup3 = (1, 2, 3, 4, 5, 6, 7)
print("tup2[0]:", tup2[0])
print("tup3[1:5]:", tup3[1:5])
