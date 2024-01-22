
class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, fly):
        self.__name = name
        self.fly=fly
    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self, target):
        return self.__name + "+" +target.__name

class NoFly(FlyingBehavior):
    def fly(self):
        return "하늘을 날 수 없습니다."

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return "하늘을 날 수 있습니다."

class Charizard(Pokemon):
    pass

class Gyarados(Pokemon):
    pass

nofly = NoFly()
g1 = Gyarados("갸라도스", nofly)
wings=FlyWithWings()
c1 = Charizard("리자몽", wings)
print(c1.fly.fly())
print(g1.fly.fly())

print(g1)
print(c1)
print(g1+c1)