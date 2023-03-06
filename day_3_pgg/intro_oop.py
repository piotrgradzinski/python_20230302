# day_3_pgg/intro_oop
from pprint import pprint


class Person:
    ...


osoba1 = Person()
osoba1.first_name = 'Piotr'
osoba1.last_name = 'GG'

print(osoba1)
print(osoba1.first_name)
print(osoba1.last_name)

osoba2 = Person()
# print(osoba2.first_name)  # AttributeError: 'Person' object has no attribute 'first_name'


class Person:
    greeting = 'Hi'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe(self, greeting='Hello'):
        print(f"{greeting}! I am {self.first_name}")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Person(first_name="{self.first_name}", last_name="{self.last_name}")>'


osoba1 = Person('Jan', 'Kowalski')
osoba1.describe('Hey')

osoba2 = Person('Ala', 'Nowak')
osoba2.describe()

# konwersja z obiektu na str
print(osoba1)
print(str(osoba1))
pprint(osoba1)

# skopiowane z tego, co wyświetliło __repr__
osoba3 = Person(first_name="Jan", last_name="Kowalski")

print('-' * 30)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    @property
    def area(self):
        return self.width * self.height


p = Rectangle(10, 20)
print(p.get_area())
print(p.area)

print('-' * 30)

"""
Wyjątki
https://docs.python.org/3/library/exceptions.html
BaseException
    Exception
        LookupError
            IndexError
            KeyError
"""
try:
    # my_list = [1, 2, 3]
    # my_list[100]
    my_dict = {'a': 100}
    my_dict['trololo']
except IndexError as e:
    print('IndexError', type(e))
except LookupError as e:
    print('LookupError', type(e))
except Exception as e:
    print('Exception', type(e))
