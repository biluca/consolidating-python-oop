import csv
from model.object import Object


class Item(Object):

    def __init__(self, description: str, price: float, quantity: int):
        super().__init__()
        self.description = description
        self.price = price
        self.quantity = quantity
        self.validate()

        self.calculate_total_price()

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"Item({self.description}, {self.price}, {self.quantity})"

    def calculate_total_price(self):
        self.__total = self.price * self.quantity
    

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        self.__total = total

    def validate(self):
        assert type(self.price) == float, "Price needs to be a Float Value"
        assert self.price >= 0, "Price needs to be greater or equals to 0 (Zero)"
        assert type(self.quantity) == int, "Quantity needs to be a Int Value"
        assert self.quantity >= 0, "Quantity needs to be greater or equals to 0 (Zero)"

    @classmethod
    def instantiate_from_csv(cls, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                item.get('description'),
                float(item.get('price')),
                int(item.get('quantity'))
            )

    @staticmethod
    def is_float(value):
        return isinstance(value, float)
