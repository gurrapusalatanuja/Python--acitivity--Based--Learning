
n = int(input("Enter number of areas: "))

areas = []

for i in range(n):
    name = input("Enter area name: ")
    demand = int(input("Enter required supplies: "))
    priority = int(input("Enter priority (1, 2, 3): "))

    areas.append([name, demand, priority])

areas.sort(key=lambda x: x[2])

print("\nAllocation Report")

for a in areas:
    allocated = min(stock, a[1])
    shortage = a[1] - allocated
    stock = stock - allocated

    print("Area:", a[0])
    print("Allocated:", allocated)
    print("Shortage:", shortage)

print("Remaining Stock:", stock)
