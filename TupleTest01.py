#! /usr/bin/python3
# Author:yang
# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 16:54
# @Author: yang
# @Site: 
# @File: TupleTest01
# @Software: PyCharm

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的
tup1[0] = 110

tup3 = tup1 + tup2
print(tup3)
