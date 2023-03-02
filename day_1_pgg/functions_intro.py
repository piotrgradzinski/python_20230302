"""
Functions intro

https://realpython.com/python-type-checking/
"""
from numbers import Number
from pprint import pprint

# type hinting
my_number: int = 10

wartosc = 123.456
print(f"{wartosc:.2}")
print("a=%f, b=%f" % (10, 20))
print("a={a}, b={b}".format(a=10, b=20))
print("a={}, b={}".format(10, 20))

print('-' * 10)

wartosc = 1230.456
print(f">{wartosc:10.2f}<")
print(f">{wartosc:^10.2f}<")
print(f">{wartosc:_^10_.2f}<")
print(f">{wartosc:_^10,.2f}<")

my_number = 10_674_231
print(my_number)

"""
ta zmienna wcześniej została opisana type hint int i dlatego PyCharm podpowiada, żeby przypisujemy niepoprawny typ
"""
my_number = 10_674_231.123
print(my_number)

from typing import Union, Optional, List, Tuple, Dict, Iterable, Sequence, Any


# def greeting(first_name: str, last_name: str,
#              age: Union[int, float] = 0) -> str:
# def greeting(first_name: str, last_name: str,
#              age: Number = 0) -> str:
def greeting(first_name: str, last_name: str,
             age: Optional[Number] = None) -> str:
    """Prepare special form of greeting.

    Some more information on the topic...

    :param first_name: Users first name
    :param last_name: Users last name
    :param age: Users age
    :return: Formatted string
    """
    return f"{first_name} {last_name} ({age:.2f})!"


print(greeting('Piotr', 'GG', 18))
print(greeting('Piotr', 'GG', 18.5))
print(greeting('Piotr', 'GG', 1j+3))  # complex, liczba zespolona https://pl.wikipedia.org/wiki/Liczby_zespolone
# print(greeting('Piotr', 'GG', 'asd'))

names: List[str] = ['Ala', 'Ela', 'Ola']
numbers: Tuple[int, int, int] = (1, 2, 3)
options: Dict[str, bool] = {'marketing': True}

"""
Iterable - wszystkie typy, które implementują interfejs iteratora, czyli takie, po których można iterować forem
Sequence - typy, w których kolejność elementów jest zachowana - np. list, tuple, dict, ale już set nie.
"""
# def square(elements: Iterable[Union[float, int]]) -> List[float]:
def square(elements: Sequence[Union[float, int]]) -> List[float]:
    return [x ** 2 for x in elements]


print(square([1, 2, 3]))
print(square((1, 2, 3)))
print(square({1, 2, 3}))


import random

def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)


print(choose([1, 2, 3, 4, 5]))


print('-' * 30)


def greeting(first_name, last_name, age=0.0):
    return f"{first_name} {last_name} ({age:.2f})!"


# argumenty pozycyjne (positional arguments)
print(greeting('Piotr', 'GG', 10))
print(greeting('Piotr', 'GG'))

# argumenty nazwane (key-worded arguments)
print(greeting(first_name='Piotr', last_name='GG', age=10))
print(greeting(first_name='Piotr', last_name='GG'))
print(greeting(last_name='GG', age=1, first_name='Piotr'))

# mieszane
print(greeting('Piotr', age=1, last_name='GG'))
# najpierw pozycyjne, później nazwane
# print(greeting(age=1, 'Piotr', last_name='GG'))

print('-' * 30)

def zliczacz(*args, **kwargs):
    pprint(args)
    pprint(kwargs)


zliczacz()
zliczacz(1, 2, 3)
zliczacz('a', 'b', 1, 2, 3)
zliczacz(1, 2, a=10, b=20, c=30)

print('-' * 30)


def srednia(*args):
    return sum(args) / len(args)


print(srednia(5, 6, 7))


print('-' * 30)


def my_fun(param, data=[1, 2, 3]):
    data.append(param)
    return data

print(my_fun(10))  # [1, 2, 3, 10]
print(my_fun(20))  # [1, 2, 3, 20]
print(my_fun(30))  # [1, 2, 3, 30]

def my_fun(param, data=None):
    # data = data or [1, 2, 3]
    # albo
    if not data:
        data = [1, 2, 3]

    data.append(param)
    return data

print(my_fun(10, [10, 20, 30]))  # [1, 2, 3, 10]
print(my_fun(20))  # [1, 2, 3, 20]
print(my_fun(30))  # [1, 2, 3, 30]








