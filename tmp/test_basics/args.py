# coding:utf-8
# Name:args.py
# Author:nigo
# Time:2022/10/12 2:06 下午 
# Description:
def test1(a,b=2,*args):
    print((a, b, args))

test1(1,)
test1(1,2)
test1(1,3)
test1(1,3,3,3,3)
test1(2,*(1,2,3,4))
test1(2,*[1,2,3,4,6])