class NigoTest:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def delName(self):
        self.__name = "xxx"

    # # property() 可以实现在不破坏类封装原则的前提下，让开发者依旧使用  实例对象.属性  的方式操作类中的属性
    # name = property(getName, setName, delName, "this is a description")
    #
    #
    # print(NigoTest.name.__doc__)
    # blog = NigoTest("nigo")
    # print(blog.name)
    # blog.name = "bigo"
    # print(blog.name)
    # del blog.name
    # print(blog.name)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        print("删除 __name")
ΩΩΩ

blog = NigoTest("nigo")
print(blog.name)
blog.name = "bigo"
print(blog.name)
del blog.name
print(blog.name)ΩΩΩ
