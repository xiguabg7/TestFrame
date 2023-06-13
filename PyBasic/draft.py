# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# '''
# @Project ：TestFrame
# @File    ：draft.py
# @Author  ：nigo
# @Date    ：2023/5/11 14:17
# '''
# # import os.path
from tmp.demo.open import met
# #
# #
# # def tests():
# #     global vars
# #     vars = 6
# #
# # print(vars)
# #
# # print(os.path.dirname(os.path.realpath(__file__)))
# #
# # if __name__ == '__main__':
# #     tests()
# #     print(vars)
# #

# # from collections import Counter
x = {'a':5,'b':3}
y = {'a':1,'c':6}
# # a = {1,2,3,3}
# # b = {3}
from collections import Counter

print(dict(Counter(x) + Counter(y)))

print(5//2)
# # print(dict(Counter(x) + Counter(y)))
# # print(dict(Counter(a) + Counter(b)))
# # print(a-b)
# str = " nigo.su @ yuan"
# print(str.index("s",3,10))
# print(str.find("y", 0, 10))
# print(str.count("n"))
# print(str.split(" ", 1))
# print(str.strip(" "))
# print(str.rstrip(" "))
# print(str.replace("n", "s", 1))
# list1 = ["12","33","44"]
# print(" ".join(list1))
# print(str.upper())
# print(str.lower())
# print(str.startswith("n"))
# print(str.endswith("n"))
# print(str.isdigit())
# print(str.isalpha())
# str2 = """
# 123
# 456
# 789
# """
#
# print(str2.splitlines())
# print(str2.splitlines(True))
# print("%3d %04.2f %-3d"%(1,2.111,44.1),"end")
# print("字符串宽10位，截取两位  %10.2s " % "hello.world")
# print("浮点数保留两位小数，宽5位，不足补0：%04.2f  " % 2.222)
# print("{}!1{:0>6.2f}".format( "1",13.9987))
# print(r"xxx/n")
# list = [1,2,3,4,6,7,True]
# print(list[::-1])
# print(len(list))
# print(max(list))
# list.append(444)
# print(list)
# list.pop()
# print(list)
# from collections import deque
# queue = deque([11,22,33])
# queue.append(44)
# print(queue.popleft())
# print(queue)

print("##### dict #####")
dict_ = {}
dict_["name"] = "zhang"
dict_["age"] = 18
dict_["telephone"] = "13100001111"
dict_.update({"telephone":"13100001112"})
dict_.update({"name": "zhang1"})
print(dict_.get("name"))
print(dict_.get("telephone"))
print(dict_.get("log","默认"))
print(dict_.pop("age"))
dict_.update([("3",4),("5",6)])
dict_.update(y=3,x=3)
print("#####遍历字典#####")
for key in dict_:
    print(key)
for value in dict_.values():
    print(value)
for item in dict_.items():
    key = item[0]
    value = item[1]
    print('%s:%s' %(key, value))

for key,value in dict_.items():
    print('%s:%s' %(key, value))

print("#####set#####")

set1 = {"a","b","a","d","e","f","g"}
print(set1)
set2 = set()
set2.add("b")
print(set2,type(set2))
print('c' in set1)
print(len(set1))
set1.add("f")
set1.remove("a")
print(set1.difference(set2))
print(set1)

from copy import copy,deepcopy
set3 = copy(set1)
set4 = deepcopy(set1)
old_list = [1,2,[4,3]]
new_list = old_list[:]
new_list1 = list(old_list)
new_list2 = old_list.copy()
old_list.insert(3,5)
print(old_list)
