class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"名字:{self.name} 体重:{self.weight} 都爱跑步"

    def run(self):
        self.weight -= 0.5
        print(self.name + "跑步，体重减少0.5")

    def eat(self):
        self.weight += 1
        print(self.name + "吃饭，体重增加1")


xiaoming = Person("小明", 50)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaohong = Person("小红", 48)
print(xiaohong)
xiaohong.run()
xiaohong.eat()
print(xiaohong)
