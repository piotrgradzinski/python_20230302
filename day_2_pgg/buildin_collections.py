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

print('-' * 30)

# defaultdict
"""
Chcę wyciągnąć wszystkie produkty i stworzyć słownik
o takiej strukturze:
{
    category_id: [product1, product2]  # lista produktów z tej kategorii
}
"""
from data.products import products

# wersja bez defaultdict
categories = {}
for p in products:
    if p['category_id'] not in categories:
        categories[p['category_id']] = []

    categories[p['category_id']].append(p)

print(categories)

# wersja z defaultdict
from collections import defaultdict

categories = defaultdict(list)
for p in products:
    categories[p['category_id']].append(p)

print(categories)

for category_id, pic in categories.items():
    print(category_id, pic)

print('-' * 30)

"""
{
    "product_id": 1, 
    "product_name": "G.Skill Ripjaws V Series", 
    "description": "Speed:DDR4-3000,Type:288-pin DIMM,CAS:15,Module:8x8GB,Size:64GB", 
    "standard_cost": 450.36, 
    "list_price": 640.99, 
    "category_id": 5
},
"""

from collections import namedtuple

Product = namedtuple('Product', ['product_id', 'product_name', 'description', 'standard_cost', 'list_price', 'category_id'])

product_1 = Product(1, "G.Skill Ripjaws V Series", "Speed:DDR4-3000,Type:288-pin DIMM,CAS:15,Module:8x8GB,Size:64GB", 450.36, 640.99, 5)

print(product_1)
print(product_1.description)

product_1 = Product(*products[0].values())
print(product_1)
print(product_1.description)

print(products[0].keys())
print(products[0].values())
print(products[0].items())
print(products[0].get('category_id', -1))  # nie znajdzie to odda None (domyślnie) albo drugi argument
print(products[0]['category_id'])  # nie znajdzie to będzie KeyError

print('-' * 30)

from collections import Counter
category_ids = [p['category_id'] for p in products]
print(category_ids)

my_counter = Counter(category_ids)
for value, counts in my_counter.items():
    print(value, counts)
