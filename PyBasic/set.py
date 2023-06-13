#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：set.py
@Author  ：nigo
@Date    ：2023/6/9 17:00 
'''
set1 = {1,2,5,8,2,0,9}
print(set1)
set1.add(10)
set1.remove(1)
print(set1)
set1.pop()
print(set1)
print(set1.difference({2, 3, 5, 8, 9}))
print(set1.intersection({2, 5}))
print(set1.union({11}))
