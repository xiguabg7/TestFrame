# coding:utf-8
# Name:test_order.py
# Author:nigo
# Time:2021/3/22 6:41 下午 
# Description:
import pytest


# @pytest.fixture(scope="module", autouse="true")
# def open():
#     print("open bro")
#     yield
#     print("down")
class TestOrder:
    # order定义执行顺序，order=0 1 2 -1
    @pytest.mark.run(order=2)
    # first定义执行顺序
    # @pytest.mark.first
    def test_one(self):
        print("one")

    @pytest.mark.run(order=3)
    def test_two(self):
        print("two")

    @pytest.mark.run(order=1)
    def test_three(self):
        print("three")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_order.py"])
