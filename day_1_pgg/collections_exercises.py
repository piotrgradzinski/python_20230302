# Collections exercises
from pprint import pprint

from data.products import products

# Listę produktów z kategorii 5, droższe niż 500.
filtered_products = [p for p in products if p['category_id'] == 5 and p['list_price'] > 500]
pprint(filtered_products)

# Lista z wysokościami marż dla wszystkich produktów
margins = [p['list_price'] - p['standard_cost'] for p in products]
pprint(margins)

# Jakie mamy kategorie produktów?
categories = {p['category_id'] for p in products}
pprint(categories)

print('-' * 30)

# description = products[0]['ALA MA KOTA']  # KeyError
# description = products[0].get('ALA MA KOTA')
# description = products[0].get('ALA MA KOTA', -1)
description = products[0].get('description')
print(description)

# Speed:DDR4-3000,Type:288-pin DIMM,CAS:15,Module:8x8GB,Size:64GB
parameters = {}
for param_pair in description.split(','):
    param_type, param_value = param_pair.split(':')
    parameters[param_type] = param_value

pprint(parameters)

# Jakie mamy typy parametrów wśród wszystkich produktów
param_types = set()
for product in products:
    for param_pair in product['description'].split(','):
        param_types.add(param_pair.split(':')[0])

pprint(param_types)

# To jest dobry przykład, kiedy nie używać comprehenions
# https://towardsdatascience.com/5-wrong-use-cases-of-python-list-comprehensions-e8455fb75692
param_types = {param_pair.split(':')[0] for product in products for param_pair in product['description'].split(',')}

pprint(param_types)