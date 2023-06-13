#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：dict.py
@Author  ：nigo
@Date    ：2023/6/9 16:27 
'''
dict1 = {"name":"li","age":"17"}
print(dict1.get("name"))
dict1.update({"name":"liyuan"})
dict1["com"] = "ses"
dict1.pop("name")

print(list(dict1))
print(dict1)

dict2 = dict([("na",1),("me",2)])
dict3 = dict(na = 12,age = 13)
dict4 = dict({"na":"144","la":"33"})
print(dict2,dict3,dict4)