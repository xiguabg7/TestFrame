# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def say(self, action):
#         self.action = action
#         print(self.name, self.age, self.gender, action)
#
#
# xiaoming = Person("小明", 20, "男")
# xiaoming.say("开车")


class Blog:
    num = 0
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return "name is %s" % self.name
    def pob(self):
        print(self.num)

    def __repr__(self):
        return "name is " + self.name

    @classmethod
    def pod(cls):
        print("cls file")
        cls.pob(cls)


blog = Blog("zhang")
# print(blog)
# print(str(blog))
# print(repr(blog))
blog.pod()