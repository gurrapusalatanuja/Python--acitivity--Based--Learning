n = int(input("Enter number of participants: "))

for i in range(n):
    name = input("Enter participant name: ").lower()
    fee = float(input("Enter registration fee: "))

    if name in participants:
        print("Duplicate Registration!")
    else:
        participants.append(name)
        total_fees += fee

sponsorship = float(input("Enter sponsorship amount: "))
expenses = float(input("Enter total expenses: "))

total_income = total_fees + sponsorship
balance = total_income - expenses

print("\nFestival Financial Report")

print("Total Participants:", len(participants))
print("Total Registration Fees:", total_fees)
print("Sponsorship Amount:", sponsorship)
print("Total Income:", total_income)
print("Total Expenses:", expenses)
print("Final Balance:", balance)

if balance >= 0:
    print("Financial Status: Profit")
else:
    print("Financial Status: Loss")
