class Person:
    __num = 0

    def __init__(self, name):
        self.__name = name

    def __getName(self):
        print("name is ", self.__name)


print(Person._Person__num)

person = Person("zhangsan")
print(person._Person__name)
person._Person__getName()
