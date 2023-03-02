# collections_intro

"""
Comprehensions
https://realpython.com/lessons/generalized-list-comprehension-structure/
"""
from pprint import pprint

numbers = []
for number in range(1, 11):
    numbers.append(number ** 2)

pprint(numbers)

# list comprehension
numbers = [number ** 2 for number in range(1, 11)]
pprint(numbers)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [x * 10 if x > 5 else x * -10 for x in nums if x % 2 == 0]
pprint(result)

result = []
for x in nums:
    if x % 2 == 0:
        result.append(x * 10 if x > 5 else x * -10)
pprint(result)

# set comprehensions
# sets: https://realpython.com/python-sets/
letters = {letter for letter in 'Ala ma kota'}
pprint(letters)
pprint(letters.intersection({'a', 'b', 'c'}))  # część wspólna, przecięcie

# dict comprehension
text = 'Ala ma kota'
occurrences = {letter: text.count(letter) for letter in text}
pprint(occurrences)

# generator expression
"""
- jednorazowy, po wyczerpaniu robimy nowy
- generator wylicza kolejne wartości w sposób leniwy (lazy evaluation)
- efektywny pamięciowo
- przydatny przy przetwarzaniu dużych zbiorów danych
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = (number ** 2 for number in numbers)
pprint(generator)
print(type(generator))

for number in generator:
    print(number)

print('-' * 30)

for number in generator:
    print(number)

generator = (number ** 2 for number in numbers)
print(next(generator))
pprint(list(generator))
# print(next(generator))

print('-' * 30)

generator = (number ** 2 for number in numbers)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
