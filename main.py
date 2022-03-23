class Human:
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age
    def hair(self):
        return "шатен"

class Boy(Human):
    def __init__(self, height, weight, age, sex, hair):
        super().__init__(height, weight, age)  # позволяет использовать __init__ в наследуемом классе!
        # передача параметров в родительский класс при инициализации боя
        self.sex = 'm'
        self.hair = "темные"
    def old(self):
        return self.age + 1
    # def color(self):
    #     return self.hair()
    # def hair(self): # перегрузка функции родительского класса
    #     return "русый"


class Petya(Boy):
    def __init__(self, height, weight, age, sex, hair):
        super().__init__(height, weight, age, sex, hair)

#
# print(Boy().old())
# print(Boy().hair())
# print(Petya().hair())

class Girl(Human):
    def __init__(self, height, weight, age, sex, hair):
        super().__init__(height, weight, age)  # позволяет использовать __init__ в наследуемом классе!
        # передача параметров в родительский класс при инициализации боя
        self.sex = 'f'
        self.hair = "темные"
    def old(self):
        return self.age + 1

class Vanya:  # пример компоозиции
    def __init__(self):
        self.param = Boy().hair

print(Boy(120, 80, 13, 'm', 'темный').old())
print(Girl(130, 34, 11, 'f', 'темный').old())


# class Scanner:
#     def can_s(self):
#         return True
#
# class Printer:
#     def can_p(self):
#         return True
#
# class MFU (Scanner, Printer):
#     def __init__(self):
#         super(Scanner, self).__init__(True)
#     def can(self):
#         print(self.can_p())
#         print(self.can_s())
#
# MFU.can(True)

class Cat:
    def say(self):
        print('meow')

class Dog:
    def say(self):
        print('wof')

class Cow:
    def say(self):
        print('moo')

if __name__ == "__main__":  # убирает косвенное выполнение файла (при подключеннии данного как модуля)

    a = (Cat(), Dog(), Cow())  # пример утиной типизации - т.к. в классической есть родительский класс с неким методом
    for animal in a:
        animal.say()