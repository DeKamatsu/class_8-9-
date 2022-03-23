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

d = re.findall(r"\d{3}", 'hdkdtk2465724 yryj4')
print(d)