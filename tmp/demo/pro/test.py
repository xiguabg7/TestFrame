# lists1 = [1, 2, 3, 4, 5, [1, 2, 3]]
# lists2 = lists1[:]
# lists1[5].append(4)
# print(lists1, lists2, id(lists1), id(lists2))
#
#
# lists1 = [1, 2, 3, 4, 5]
# lists2 = lists1[:]
# lists1.append(6)
# print(lists1, lists2, id(lists1), id(lists2))
from typing import Iterable, Iterator

#
# lists = [1, 2, 3, 4, 5]
# print(isinstance(enumerate(lists), Iterable))
#
# for i,j in enumerate(lists):
#     print(i,j)

a = "asdf"
b = 12431
c = (1,2,3)
d = {"a":"1","b":"2"}
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))

# res = [i*i for i in range(0,11) if i % 2 == 0]
# print(res)
# res = [(k,v) for k,v in d.items()]
# print(res)

l = (i for i in range(10))
print(l)
# print(l.__next__())
print(isinstance(iter(l),Iterator))
print(isinstance(l, Iterator))
print(isinstance(l,Iterable))

# def odd():
#     print('step 1')
#     return
#     # yield 1
#     print('step 2')
#     print('step 3')
# o = odd()
# for i in o:
#     print(i)




