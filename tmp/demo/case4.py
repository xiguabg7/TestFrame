class Gun:
    def __init__(self, name):
        self.__name = name
        self.__bullet_count = 0

    def __str__(self):
        return f"枪名{self.__name}有子弹{self.__bullet_count}颗"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def bullet_count(self):
        return self.__bullet_count

    @bullet_count.setter
    def bullet_count(self, count):
        self.__bullet_count += count

    def shoot(self):
        if self.__bullet_count <= 0:
            print(self.__name + "子弹数量不足")
            return
        print(f"{self.__name}发射子弹")
        self.__bullet_count -= 1


class Solider:
    def __init__(self, name):
        self.__name = name
        self.__gun = None

    def __str__(self):
        # print(f"士兵持有枪支{self.__gun.name},剩余{self.__gun.bullet_count}颗子弹")
        return f"士兵持有枪支{self.__gun.name},剩余{self.__gun.bullet_count}颗子弹"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def gun(self):
        return self.__name

    @gun.setter
    def gun(self, gun):
        self.__gun = gun

    def fire(self):
        # if self.__gun is None:
        #     print("无枪")
        if self.__gun.bullet_count == 0:
            print("无子弹")
        self.__gun.bullet_count += 10
        self.__gun.shoot()

ak47 = Gun("ak47")

print(ak47)

# 声明一个士兵
xusanduo = Solider("许三多")
# 给士兵带上 AK47！
xusanduo.gun = ak47
# 开火！
xusanduo.fire()

print(xusanduo)