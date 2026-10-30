# Campus Festival Registration and Financial Audit Using Python

## 1. Problem Statement
Campus Festival Registration and Financial Audit: Reconcile participant lists, registration fees, 
sponsorship contributions, and expenses; detect duplicate registrations and calculate the final 
financial balance. 
## 2. Algorithm

1. Start the program.
2. Enter the number of participants.
3. Enter participant names and registration fees.
4. Check for duplicate registrations.
5. Accept only unique participants.
6. Calculate total registration fees.
7. Enter sponsorship contributions.
8. Enter festival expenses.
9. Calculate total income and total expenses.
10. Calculate the final financial balance.
11. Display the results.
12. Stop the program.

## 3. Flowchart Using Mermaid

flowchart TD
    A([Start]) --> B[/Enter participant details/]
    B --> C{Duplicate name?}
    C -- Yes --> D[Reject registration]
    C -- No --> E[Add participant and fee]
    D --> F{More participants?}
    E --> F
    F -- Yes --> B
    F -- No --> G[/Enter sponsorship and expenses/]
    G --> H[Calculate total income]
    H --> I[Calculate final balance]
    I --> J[Display audit report]
    J --> K([Stop])


## 5. Sample Input

```
Enter number of participants: 3

Enter participant name: Ravi
Enter registration fee: 500

Enter participant name: Anu
Enter registration fee: 500

Enter participant name: Ravi
Enter registration fee: 500

Enter sponsorship amount: 5000
Enter total expenses: 3000
```

## 6. Sample Output

```
Duplicate Registration!

Festival Financial Report

Total Participants: 2
Total Registration Fees: 1000.0
Sponsorship Amount: 5000.0
Total Income: 6000.0
Total Expenses: 3000.0
Final Balance: 3000.0

Financial Status: Profit
```

