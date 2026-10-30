name = input("Enter chemical name: ")
category = input("Enter category: ")
quantity = float(input("Enter quantity: "))

if category == "Flammable":
    limit = 50
elif category == "Corrosive":
    limit = 40
elif category == "Oxidizer":
    limit = 30
elif category == "General":
    limit = 100
else:
    limit = 0

if limit == 0:
    print("Invalid Category")
elif quantity < 0 or quantity > limit:
    print("Invalid Quantity")
elif category == "Oxidizer":
    print("Check compatibility before storage")
else:
    print("Chemical Inventory is Valid")

