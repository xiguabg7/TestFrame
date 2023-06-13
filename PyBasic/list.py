#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：list.py
@Author  ：nigo
@Date    ：2023/6/9 15:46 
'''
list1 = [1,2,3,3,8,6,1,0,8]
print(list1.append(10))
print(list1)
print(list1.extend((1,4,5,11)))
print(list1)
print(list1.insert(0,5))
print(list1)
print(list1.remove(8))
print(list1)
print(list1.pop(1))
print(list1)
print(list1.count(3))
list1.sort()
print(list1)
list1.reverse()
print(list1)
