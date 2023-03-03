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






