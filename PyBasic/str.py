#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestFrame 
@File    ：str.py
@Author  ：nigo
@Date    ：2023/6/8 17:09 
'''
str1 = " hello message "
str2 = "hello\n m\r\ne\nssag\re "

print(str1.index("m", 0, 10))
print(str1.find("m"))
print(str1.count("e"))
print(str1.split("e",2))
print(str2.splitlines())
print(str1.strip(" "))
print(str1.replace("e","a",1))
# 将列表、元组转成字符串
print("~".join(str1))
print(str1.upper())
print(str1.lower())
print(str1.isdigit())
print(str1.isalpha())

print("{} {}".format("1","2"))
print("浮点数{:0>+9.2f}".format(123.19))
