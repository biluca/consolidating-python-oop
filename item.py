class Item:

    all = []
    default_discount = 0.9
    discount_limit = 700.00

    def __init__(self, description: str, price: float, quantity: int):
        self.description = description
        self.price = price
        self.quantity = quantity
        self.validate()

        self.calculate_total_price()
        Item.all.append(self)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f"Item({self.__str__()})"

    def calculate_total_price(self):
        if (self.price > self.discount_limit):
            self.total = self.price * self.quantity * self.default_discount
        self.total = self.price * self.quantity

    def validate(self):
        assert type(self.price) == float, "Price needs to be a Float Value"
        assert self.price >= 0, "Price needs to be greater or equals to 0 (Zero)"
        assert type(self.quantity) == int, "Quantity needs to be a Int Value"
        assert self.quantity >= 0, "Quantity needs to be greater or equals to 0 (Zero)"


item1 = Item("Redmi Note 9", 500.00, 1)
item2 = Item("Dell Inspiron 14500", 1000.33, 3)
item3 = Item("Playstation Dualshock - Black", 299.50, 2)

print(Item.all)

for item in Item.all:
    print(item)
