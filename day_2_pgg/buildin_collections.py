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

