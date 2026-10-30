# Food Waste Monitoring System Using Python

## 1. Problem Statement
. Food Waste Monitoring System: Compare prepared meals, meals served, and leftovers across 
several days; calculate wastage percentages and identify days exceeding acceptable limits.

## 2. Algorithm

1. Start the program.
2. Enter the number of days.
3. Enter prepared meals and served meals for each day.
4. Calculate leftover meals.
5. Calculate wastage percentage.
6. Check whether wastage exceeds 10%.
7. If it exceeds 10%, display High Waste.
8. Otherwise, display Acceptable Waste.
9. Display the results.
10. Stop the program.

## 3. Flowchart Using Mermaid

flowchart TD
    A([Start]) --> B[/Enter number of days/]
    B --> C[/Enter prepared and served meals/]
    C --> D[Calculate leftover meals]
    D --> E[Calculate wastage percentage]
    E --> F{Waste above 10%?}
    F -- Yes --> G[High Waste]
    F -- No --> H[Acceptable Waste]
    G --> I[/Display results/]
    H --> I
    I --> J([Stop])


## 5. Sample Input

```
Enter number of days: 3

Day 1
Enter prepared meals: 100
Enter served meals: 90

Day 2
Enter prepared meals: 120
Enter served meals: 100

Day 3
Enter prepared meals: 150
Enter served meals: 145
```

## 6. Sample Output

```
Food Waste Monitoring System

Day 1
Leftover meals: 10
Wastage percentage: 10.0 %
Acceptable Food Waste

Day 2
Leftover meals: 20
Wastage percentage: 16.67 %
High Food Waste

Day 3
Leftover meals: 5
Wastage percentage: 3.33 %
Acceptable Food Waste

Food Waste Analysis Completed
```

