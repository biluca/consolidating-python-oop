import csv
from model.item import Item


class Phone(Item):

    def __init__(self, description: str, price: float, quantity: int, touch_screen: bool):
        super().__init__(description, price, quantity)
        self.touch_screen = touch_screen

    def __repr__(self) -> str:
        return f"Phone({self.description}, {self.price}, {self.quantity}, {self.touch_screen})"

    @classmethod
    def instantiate_from_csv(cls, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            phones = list(reader)

        for phone in phones:
            Phone(
                phone.get('description'),
                float(phone.get('price')),
                int(phone.get('quantity')),
                bool(phone.get('touch_screen')),
            )
