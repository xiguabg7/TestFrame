# coding:utf-8
# Name:unpack.py
# Author:nigo
# Time:2022/10/12 6:20 下午 
# Description:
# 集合解包
a, b, c = {2, 5, 8}
print(a, b, c)
# 元组解包
a, b, c = (1, 2, 3)
print(a, b, c)
# 列表解包
a, b, c = [2, 3, 4]
print(a, b, c)
# 字典解包
a, b, c = {"a": 1, "b": 2, "c": 3}
print(a, b, c)
# 字符串解包
a, b, c = "tfg"
print(a, b, c)
# 生成器解包
a, b, c = (x + 1 for x in range(3))
print(a, b, c)
