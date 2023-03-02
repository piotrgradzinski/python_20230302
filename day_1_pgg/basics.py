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






