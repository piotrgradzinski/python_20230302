# oop_exercises

"""
Na podstawie produktu z data/products.py
stwórz klasę reprezentującą ten produkt.
"""
from data.products import products


class Product:
    def __init__(self, product_id, category_id, product_name, description, standard_cost, list_price):
        self.product_id = product_id
        self.category_id = category_id
        self.product_name = product_name
        self.description = description
        self.standard_cost = standard_cost
        self.list_price = list_price

    def __str__(self):
        return f"{self.product_name}({self.product_id})"

    @classmethod
    def create_from_dict(cls, data: dict):
        # return Product(**data)
        return cls(**data)


p = Product(product_id=1, product_name="G.Skill Ripjaws V Series", description="Speed:DDR4-3000", standard_cost=450.36, list_price=640.99, category_id=5)
print(p)

p = Product.create_from_dict(products[1])
print(p)
print(p.product_id, p.product_name, p.standard_cost)

products_oop = [Product.create_from_dict(p) for p in products]
print(products_oop)