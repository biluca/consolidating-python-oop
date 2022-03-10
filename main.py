from item import Item, Phone, Object

Item.instantiate_from_csv("items.csv")

phone1 = Phone("iPhone IX", 9999.98, 2, True)
phone2 = Phone("Nokia 2220", 150.49, 3, False)


print(Item.all)
print("---")
print(Phone.all)
print("---")
print(Object.all)