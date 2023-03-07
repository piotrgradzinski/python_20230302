import sys

my_list = [1, 2]

print(id(my_list))
print(sys.getrefcount(my_list))

my_list2 = my_list
print(sys.getrefcount(my_list))

my_list2 = None
print(sys.getrefcount(my_list))

"""
Jak działa porównywanie obiektów w Pythonie
== - porównujemy wartości, wykorzystywane jest __eq__
    x == y -> x.__eq__(y) 
is - identity, referencje, adres w pamięci
in - https://docs.python.org/3/reference/expressions.html#membership-test-operations
    x in y is equivalent to any( x is e or x == e for e in y )
    
https://docs.python.org/3/glossary.html#term-hashable
"""

var1 = [10, 20]
var2 = var1
var3 = var1
var4 = [10, 20]

print(var1 == var2)  # True
print(var1 is var2)  # True

print(var1 == var4)  # True
print(var1 is var4)  # False

print('-' * 30)

print({1, 2, 3})
print({'a', 'b', 'c'})
print({1, 'a', False})
# print({[1, 2], [3, 4]})  # TypeError: unhashable type: 'list'

print('-' * 30)

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # def __hash__(self):
    #     raise TypeError()


p1 = Person('Piotr', 'GG')
p2 = Person('John', 'Doe')
my_set = {p1, p2}

print(my_set)
p1.first_name = 'Maciej'

print(my_set)


print('-' * 30)

print('a'.__hash__())
print(hash('a'))
print(hash((1, 2, 3)))
# print(hash([1, 2, 3]))
print(hash(p1))
print(hash({'a': 1}))