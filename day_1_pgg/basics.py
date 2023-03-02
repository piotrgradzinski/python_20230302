# basics.py

first_name = "Piotr"
first_name = 'Piotr'
text = """Ala
ma
kota"""
text = '''Ala
ma
kota
'''
firstName = 'Piotr'  # nie jest zgodne z PEP8



"""
and, or
https://docs.python.org/3/reference/expressions.html#boolean-operations
The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
"""
print([1] or 'Ala')
print([] or 0)

print([] and 'Ala')
print('Tomek' and 'Ala')

dane_ze_swiata = ''

db_name = dane_ze_swiata or 'my_db'
print(db_name)

# Truthy / falsy values...
"""

"""
print(bool(10))  # True
print(bool(-1))  # True
print(bool(0))  # True
print(bool('Ala ma kota'))  # True
print(bool(' '))  # True
print(bool(''))  # False
print(bool([]))  # False
print(bool(['']))  # True
print(bool(None))  # False

first_name = 'Piotr'

if first_name == 'Piotr':
    print('Czesc Piotr!')
elif first_name == 'Ala':
    print('Czesc Ala')
else:
    print('buuu')



first_name = 'Piotr'

bonus = None
if first_name == 'Piotr':
    bonus = 10
else:
    bonus = 0

# WARTOŚĆ_WYRAŻENIA_JAK_TRUE if WARUNEK else WARTOŚĆ_WYRAŻENIA_JAK_FALSE
bonus = 10 if first_name == 'Piotr' else 0
print(bonus)
