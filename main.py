from item import Item

Item.instantiate_from_csv("items.csv")
print(Item.all)