# ABC - Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hello! My name is {self.name}')

    @abstractmethod
    def emit_sound(self):
        pass

class Dog(Animal):
    def emit_sound(self):
        print('Hau hau')

class Cat(Animal):
    def emit_sound(self):
        print('Miau miau')

class Fish(Animal):
    def emit_sound(self):
        raise NotImplemented()

# animal = Animal('Cos')
# animal.say_hello()

dog = Dog('Burek')
dog.emit_sound()

cat = Cat('Mruczek')
cat.emit_sound()

fish = Fish('Nemo')
# fish.emit_sound()



"""
Enum
dla Pythona < 3.11
pip install StrEnum
"""

# < 3.11
from strenum import StrEnum

# >= 3.11
# from enum import StrEnum
class Services(StrEnum):
    ORACLE = 'oracle'
    JUPYTER = 'jupyter'



print(Services.JUPYTER)







