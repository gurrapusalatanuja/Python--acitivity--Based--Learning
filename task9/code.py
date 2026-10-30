
n = int(input("Enter number of transactions: "))

withdrawals = 0

for i in range(n):

    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Transfer")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid Amount")

    elif choice == 1:
        balance += amount
        withdrawals = 0
        print("Deposit Successful")

    elif choice == 2 or choice == 3:

        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount

            if choice == 2:
                withdrawals += 1
                print("Withdrawal Successful")
            else:
                withdrawals = 0
                print("Transfer Successful")

    else:
        print("Invalid Choice")

    if withdrawals >= 3:
        print("Warning: Suspicious Repeated Withdrawals!")

    print("Current Balance:", balance)

print("\nFinal Account Balance:", balance)
print("ATM Audit Completed")
