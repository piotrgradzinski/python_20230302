from functools import cmp_to_key

my_list = [(2, 2), (3, 4), (4, 1), (1, 3)]

# chciałbym posortować z użyciem własnego komparatora
# po drugim elemencie tupli

def komparator(a, b) -> int:
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1

print(my_list)
my_list.sort(key=cmp_to_key(komparator))
print(my_list)

print('-' * 30)

my_list = ['user-5', 'user-2', 'user-10', 'user-1']

print(my_list)
my_list.sort()
print(my_list)

from natsort import natsorted
print(natsorted(my_list))

