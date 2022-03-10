import csv


class Object:
    all = []

    def __init__(self):
        Object.all.append(self)
        


class Item(Object):

    default_discount = 0.9
    discount_limit = 700.00

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
        if (self.price > self.discount_limit):
            self.total = self.price * self.quantity * self.default_discount
        self.total = self.price * self.quantity

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


class Phone(Item):

    def __init__(self, description: str, price: float, quantity: int, touch_screen: bool):
        super().__init__(description, price, quantity)
        self.touch_screen = touch_screen

    def __repr__(self) -> str:
        return f"Phone({self.description}, {self.price}, {self.quantity}, {self.touch_screen})"
