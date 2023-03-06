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
