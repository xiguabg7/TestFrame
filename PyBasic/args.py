#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：args.py
@Author  ：nigo
@Date    ：2023/6/13 09:57 
'''
def f1(a,b=2,*args,**kwargs):
    print(type(args))
    for i in args:
        print("Optional argument:",i)
    print(type(kwargs))
    for v,j in kwargs.items():
        print("name:",v)
        print("value:",j)
    print(a,b)

f1(1,3,*(4,5,6),n=2,m=3)

def f2(a,/,b,*,c):
    print(a,b,c)
f2(1, 2, c=3)