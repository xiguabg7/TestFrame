#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：tuple.py
@Author  ：nigo
@Date    ：2023/6/9 16:19 
'''
tuple1 = (1,2,11,2)
print(tuple1.index(2))
print(tuple1.count(2))
print(len(tuple1))
tuple2 = tuple1[0:2]
print(tuple2)
print((tuple1 + tuple2))