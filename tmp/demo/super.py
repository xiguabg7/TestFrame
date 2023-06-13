class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.')


# Mammal 继承 Animal
class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a mammal.')
        super().__init__(mammalName)


# CannotFly 继承 Mammal
class CannotFly(Mammal):
    def __init__(self, mammalThatCantSwim):
        print(mammalThatCantSwim, "cannot fly.")
        super().__init__(mammalThatCantSwim)


# CannotSwim 继承 Mammal
class CannotSwim(Mammal):
    def __init__(self, mammalThatCantSwim):
        print(mammalThatCantSwim, "cannot swim.")
        super().__init__(mammalThatCantSwim)


# Cat 继承 CannotSwim 和 CannotFly
class Cat(CannotSwim, CannotFly):
    def __init__(self):
        print('I am a cat.');
        super().__init__('Cat')


# Driver code
cat = Cat()
print('')
bat = CannotSwim('Bat')
