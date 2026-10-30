available = int(input("Enter available computers: "))
n = int(input("Enter number of activities: "))
activities = []
for i in range(n):
    print("\nActivity", i + 1)

    name = input("Enter activity name: ")
    priority = int(input("Enter priority (1 is highest): "))
    required = int(input("Enter required computers: "))

    activities.append([name, priority, required
activities.sort(key=lambda x: x[1])

print("\nResource Allocation Results")

for a in activities:
    name = a[0]
    required = a[2]

    allocated = min(required, available)
    shortage = required - allocated

    available = available - allocated

    print("\nActivity:", name)
    print("Allocated:", allocated)
    print("Shortage:", shortage)

print("\nRemaining computers:", available)
