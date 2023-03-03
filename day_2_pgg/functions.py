from pprint import pprint

my_list = ['ala', 'ola', 'ela']
print(my_list)

# na wszystkich obiektach iterowalnych (iterable) możemy uruchomić *
print(*my_list)

# gdyby to zrobić ręcznie
print('ala', 'ola', 'ela')

print(*'ala ma kota')


def greeting(first_name, last_name):
    return f"{first_name} {last_name}"


params = {
    'first_name': 'Piotr',
    'last_name': 'GG',
}

# ** działają tylko na słowniku
print(greeting(**params))

# ręcznie
print(greeting(first_name='Piotr', last_name='GG'))

# łączenie słowników
first_dict = {'a': 1, 'b': 2}
second_dict = {'c': 3, 'd': 4}

merged = {**first_dict, **second_dict}
pprint(merged)

merged = {*first_dict, *second_dict}  # * na słowniku - dostajemy klucze
print(type(merged), merged)

first_list = [1, 2, 3]
second_list = [4, 5, 6]
merged = [*first_list, *second_list]
pprint(merged)


def square(number):
    return number ** 2


print(square(4))

my_square = square
print(my_square(4))
print(type(square), type(my_square))

def square(number):
    return number ** 4

def square3(number):
    return number ** 3

square = square3
print(square(3))

print(my_square(3))


def square(number):
    return number ** 2


print(square(2))

# to samo, ale z wykorzystaniem funkcji lambda

square = lambda number: number ** 2
print(square(2))


# map - mapowanie wartosci
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapped_numbers = map(lambda x: x * 10, numbers)
print(mapped_numbers)
for number in mapped_numbers:
    print(number)

mapped_numbers = map(lambda x: x * 10, numbers)
print(list(mapped_numbers))

numbers = [1, 2, 3]
names = ['Ala', 'Ela', 'Ola']  # map zatrzymuje się przy najkrótszym kontenerze

mapped = map(lambda number, name: f"{name}{number}", numbers, names)
print(list(mapped))

# wielkosc kolekcji musi się zgadzać z liczbą zmiennych, na które je przypisuje
first_name, last_name = ['Piotr', 'GG']
print(first_name, last_name)

# filter
filtered_number = filter(lambda x: x > 4, numbers)
print(list(filtered_number))

# zip
numbers = [1, 2, 3]
names = ['Ala', 'Ela', 'Ola']

print(list(zip(numbers, names)))

print('-' * 30)

# all, any
my_list = ['Ala', None, False, 0]
print(all(my_list))  # False
print(any(my_list))  # True

print('-' * 30)

from data.products import products

"""
Chciałbym sprawdzić czy we wszystkich produktach,
standard_cost jest mniejszy niż list_price, czyli, 
czy sprzedaję drożej niż kupuję.
Nad wodą = True / False?
"""
above_water = all(map(lambda p: p['standard_cost'] < p['list_price'], products))
print(above_water)
