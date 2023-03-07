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

