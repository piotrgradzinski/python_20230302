# oop_exercises
from enum import IntEnum
from pprint import pprint
from dataclasses import dataclass
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
        return self.standard_cost * (1.0 + self.MARGIN_BASIC_RATE) <= self.list_price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.product_id == other.product_id
        elif isinstance(other, int):
            return self.product_id == other
        else:
            return False

    @staticmethod
    def extract_params(data: str):
        params = {}
        for param_pair in data.split(','):
            name, value = param_pair.split(':')
            params[name] = value
        return params

products_oop = [Product.create_from_dict(p) for p in products]

@dataclass
class OrderItem:
    product: Product
    quantity: int = 1

    @property
    def price(self):
        return round(self.product.list_price * self.quantity, 2)

    def __str__(self):
        return f'{self.product.product_name} x {self.quantity} = {self.price:.2f}'

@dataclass
class OrderItemWithDiscount(OrderItem):
    discount: float = 0.1

    @property
    def price(self):
        return round(super().price * (1.0 - self.discount), 2)

    def __str__(self):
        return f'{super().__str__()} ({self.discount * 100}% discount)'

class OrderStatus(IntEnum):
    NEW = 0
    ACTIVE = 10
    CLOSED = 20

class Order:
    def __init__(self, order_items: list[OrderItem] = None, status: OrderStatus = OrderStatus.NEW):
        self._order_items: list[OrderItem] = order_items or []
        self.status = status

    def __getitem__(self, product_id) -> int:
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
            if oi.product == product_id:
                self._order_items.remove(oi)
                return
        raise ValueError('Product not found.')

    def add_product(self, product: Product, quantity: int):
        for oi in self._order_items:
            if oi.product == product:
                oi.quantity += quantity
                return

        self._order_items.append(OrderItem(product=product, quantity=quantity))

    @property
    def total_price(self):
        return sum(map(lambda oi: oi.price, self._order_items))

    def __str__(self):
        out = []
        out.append(self._str_header())
        out.append(self._str_order_item_summary())
        out.append(self._str_footer())
        return '\n'.join(out)

    def _str_header(self):

        return 'Order'

    def _str_order_item_summary(self):
        out = ['Products']
        for oi in self._order_items:
            out.append(f'\t{str(oi)}')
        return '\n'.join(out)

    def _str_footer(self):
        return f'Total: {self.total_price:.2f}'

class OrderWithDiscount(Order):
    def __init__(self, order_items: list[OrderItem] = None, discount: float = 0.5, status: OrderStatus = OrderStatus.NEW):
        super().__init__(order_items, status)
        self.discount = discount

    @property
    def total_price(self):
        return super().total_price * (1.0 - self.discount)

    # def __str__(self):
    #     return f'Discount {self.discount * 100}%\n{super().__str__()}'

    def _str_header(self):
        return f'Order with discount {self.discount * 100}%'

    def _str_footer(self):
        return f'{super()._str_footer()} (with {self.discount * 100}% discount)'


my_order_items = [
    OrderItem(product=Product.create_from_dict(products[0]), quantity=1),
    OrderItem(product=Product.create_from_dict(products[1]), quantity=1),
    OrderItemWithDiscount(product=products_oop[2], quantity=1, discount=0.5)
]

my_order = Order(order_items=my_order_items)

my_order.add_product(product=products_oop[0], quantity=10)
my_order.add_product(product=products_oop[1], quantity=30)

pprint(my_order._order_items)
print(my_order.total_price)

print('-' * 30)

print(my_order)

print('-' * 30)

my_order_wd = OrderWithDiscount(order_items=my_order_items, discount=0.5, status=OrderStatus.ACTIVE)
print(my_order_wd)
print(my_order_wd.status)
print(OrderStatus(10), type(OrderStatus(10)))



