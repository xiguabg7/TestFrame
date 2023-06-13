from typing import Callable


class NigoTest:
    def __init__(self, name):
        self.name = name

    # call 将实例对象像函数一样调用
    def __call__(self, *args, **kwargs):
        print(self.name)
        print(args)
        print(kwargs)


nigo = NigoTest("nigo")
# nigo(1, 2, 1, key="value")
nigo.__call__(1, 2, 1, key="value")
print(isinstance(nigo, Callable))
