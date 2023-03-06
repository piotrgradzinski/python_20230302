# oop_exercises

"""
Na podstawie produktu z data/products.py
stwórz klasę reprezentującą ten produkt.
"""
from pprint import pprint

from data.products import products


class Product:
    MARGIN_BASIC_RATE = 0.1  # 10%

    def __init__(self, product_id, category_id, product_name, description, standard_cost, list_price):
        self.product_id = product_id
        self.category_id = category_id
        self.product_name = product_name
        self.description = description
        self.standard_cost = standard_cost
        self.list_price = list_price

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
            raise ValueError('Minimum margin not met.')
        self.list_price = self.standard_cost + value

    @property
    def has_basic_margin(self) -> bool:
        # return self.standard_cost * (1.0 + Product.MARGIN_BASIC_RATE) <= self.list_price
        return self.standard_cost * (1.0 + self.MARGIN_BASIC_RATE) <= self.list_price


p = Product(product_id=1, product_name="G.Skill Ripjaws V Series", description="Speed:DDR4-3000", standard_cost=450.36, list_price=640.99, category_id=5)
print(p)

p = Product.create_from_dict(products[1])
# print(p)
# print(p.product_id, p.product_name, p.standard_cost)

products_oop = [Product.create_from_dict(p) for p in products]
# pprint(products_oop)

print(p.standard_cost, p.list_price, p.margin, p.has_basic_margin)
p.margin = 600
print(p.standard_cost, p.list_price, p.margin, p.has_basic_margin)
