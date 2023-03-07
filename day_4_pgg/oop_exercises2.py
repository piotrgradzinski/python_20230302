# oop_exercises

"""
Na podstawie produktu z data/products.py
stwórz klasę reprezentującą ten produkt.
"""
from pprint import pprint

from data.products import products

class MarginError(ValueError):
    pass


class Product:
    MARGIN_BASIC_RATE = 0.1  # 10%

    def __init__(self, product_id, category_id, product_name, description, standard_cost, list_price):
        self.product_id = product_id
        self.category_id = category_id
        self.product_name = product_name
        self.description = description
        self.standard_cost = standard_cost
        self.list_price = list_price
        self.params = Product.extract_params(self.description)

    def __str__(self):
        return f"{self.product_name}({self.product_id})"

    def __repr__(self):
        return f"<Product({', '.join(['%s=%r' % (k, v) for k, v in self.__dict__.items()])})>"

    @classmethod
    def create_from_dict(cls, data: dict):
        # return Product(**data)
        return cls(**data)

    @property
    def margin(self):
        return self.list_price - self.standard_cost

    @margin.setter
    def margin(self, value):
        if self.standard_cost * (1.0 + self.MARGIN_BASIC_RATE) > self.standard_cost + value:
            raise MarginError('Minimum margin not met.')
        self.list_price = self.standard_cost + value

    @property
    def has_basic_margin(self) -> bool:
        # return self.standard_cost * (1.0 + Product.MARGIN_BASIC_RATE) <= self.list_price
        return self.standard_cost * (1.0 + self.MARGIN_BASIC_RATE) <= self.list_price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.product_id == other.product_id
        elif isinstance(other, int):
            return self.product_id == other
        else:
            # return id(self) == id(other)
            return False

    @staticmethod
    def extract_params(data: str):
        params = {}
        for param_pair in data.split(','):
            name, value = param_pair.split(':')
            params[name] = value
        return params


# p = Product(product_id=1, product_name="G.Skill Ripjaws V Series", description="Speed:DDR4-3000", standard_cost=450.36, list_price=640.99, category_id=5)
# print(p)

p = Product.create_from_dict(products[0])

p1 = Product.create_from_dict(products[1])
p2 = Product.create_from_dict(products[1])
print(p1, p2)
print(type(p1), type(p2))
print(id(p1), id(p2))
print(p1 == p2)
print(p1.params)
print(p.params)

# print(p)
# print(p.product_id, p.product_name, p.standard_cost)

products_oop = [Product.create_from_dict(p) for p in products]
# pprint(products_oop)

try:
    print(p.standard_cost, p.list_price, p.margin, p.has_basic_margin)
    p.margin = 10
    print(p.standard_cost, p.list_price, p.margin, p.has_basic_margin)
# except Exception as e:
# except ValueError as e:
except MarginError as e:
    print('Unable to set margin:', e)
else:
    # uruchamiany jeśli nie było wyjątku
    print('Nie było wyjątku...')
finally:
    print('finally uruchomi się zawsze ')

print('Ala ma kota')

print('-' * 30)


from dataclasses import dataclass


@dataclass
class OrderItem:
    product: Product
    quantity: int = 1

    @property
    def price(self):
        return self.product.list_price * self.quantity


class Order:
    def __init__(self, order_items: list[OrderItem] = None):
        self._order_items: list[OrderItem] = order_items or []

    def __getitem__(self, product_id) -> int:
        # zwraca OrderItem po kluczu z listy self._order_items
        # return self._order_items[item]
        # wyszukać OrderItem taki, którego product_id == item
        for oi in self._order_items:
            if oi.product.product_id == product_id:
                return oi.quantity

        raise KeyError(f'Product {product_id} not found')

    def __setitem__(self, product_id: int, quantity: int):
        for oi in self._order_items:
            if oi.product.product_id == product_id:
                oi.quantity = quantity
                return

        raise KeyError('Product not found')

    def __delitem__(self, product_id):
        for oi in self._order_items:
            # if oi.product.product_id == product_id:
            if oi.product == product_id:
                self._order_items.remove(oi)
                return
        raise ValueError('Product not found.')

    def add_product(self, product: Product, quantity: int):
        for oi in self._order_items:
            # if oi.product.product_id == product.product_id:
            if oi.product == product:
                oi.quantity += quantity
                return

        self._order_items.append(OrderItem(product=product, quantity=quantity))

    @property
    def total_price(self):
        return sum(map(lambda oi: oi.price, self._order_items))

    def __str__(self):
        out = ['Products:']
        for oi in self._order_items:
            out.append(f'\t{oi.product.product_name} x {oi.quantity} = {oi.price:.2f}')
        out.append(f'Total: {self.total_price:.2f}')
        return '\n'.join(out)

my_order_items = [
    OrderItem(product=Product.create_from_dict(products[0]), quantity=10),
    OrderItem(product=Product.create_from_dict(products[1]), quantity=20),
]

my_order = Order(order_items=my_order_items)
print(my_order[1])  # my_order[product_id] -> quantity
try:
    print(my_order[5])
except KeyError as e:
    print(e)

print(my_order[1])
my_order[1] = 100
print(my_order[1])

try:
    my_order[5] = 500
except KeyError as e:
    print(e)

del(my_order[1])
print(my_order._order_items)

my_order.add_product(product=products_oop[0], quantity=10)
my_order.add_product(product=products_oop[1], quantity=30)

print(my_order._order_items)
print(my_order.total_price)
print(my_order)