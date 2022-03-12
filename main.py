from model.item import Item
from model.phone import Phone
from model.object import Object

Item.instantiate_from_csv("data/items.csv")
Phone.instantiate_from_csv("data/phones.csv")

# print(Item.all)
# print("---")
# print(Phone.all)
# print("---")
# print(Object.all)

for item in Item.all:
    print(item.total)
    item.total = int(item.total) + 1.0

for item in Item.all:
    print(item.total)
