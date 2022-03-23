# import!!!

import test_pack  # исполняет файл __init__.py пакета
import test_pack.tastytest
import main
from main import Cat as Kitty
import re

print(__name__)

rex = main.Dog()
rex.say()

tom = Kitty()
tom.say()

d = re.findall(r"\d{3}", 'hdkdtk2465724 yryj4')  # возвращает лист (список) с результатами
print(d)

c = re.compile(r"\d{3}")
st = 'hdkdtk2465724 yryj4'
print(re.findall(c, st))  # возвращает лист (список) с результатами


import itertools

a = itertools.count(1, 20)
for i in a:
    print(i)
    if i >100:
        break

x = itertools.combinations("sgadgehz245", 10)
for i in x:
    print(i)


