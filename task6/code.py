

n = int(input("Enter number of days: "))

for i in range(n):
    print("\nDay", i + 1)

    prepared = int(input("Enter prepared meals: "))
    served = int(input("Enter served meals: "))

    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid meal details")
        continue

    leftover = prepared - served
    waste = (leftover / prepared) * 100

    print("Leftover meals:", leftover)
    print("Wastage percentage:", round(waste, 2), "%")

    if waste > 10:
        print("High Food Waste")
    else:
        print("Acceptable Food Waste")

print("\nFood Waste Analysis Completed")
