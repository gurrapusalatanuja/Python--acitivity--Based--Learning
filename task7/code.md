# Campus Resource Allocation Under Constraints Using Python

## 1. Problem Statement
Campus Resource Allocation Under Constraints: Compare equipment requirements with 
available resources across multiple activities, calculate shortages, and produce a feasible allocation 
using a specified priority order. 


## 2. Algorithm

1. Start the program.
2. Enter the available number of resources.
3. Enter the number of activities.
4. Enter activity name, priority, and equipment requirements.
5. Sort activities according to priority.
6. Compare required resources with available resources.
7. Allocate available resources to each activity.
8. Calculate shortages.
9. Display allocated resources and shortages.
10. Stop the program.

## 3. Flowchart Using Mermaid

flowchart TD
    A([Start]) --> B[/Enter available resources/]
    B --> C[/Enter activity requirements/]
    C --> D[Sort activities by priority]
    D --> E[Check available resources]
    E --> F{Resources available?}
    F -- Yes --> G[Allocate resources]
    F -- No --> H[Calculate shortage]
    G --> I[Update available resources]
    H --> I
    I --> J{More activities?}
    J -- Yes --> E
    J -- No --> K[Display allocation results]
    K --> L([Stop])


## 5. Sample Input

```
Enter available computers: 20

Enter number of activities: 3

Activity 1
Enter activity name: Seminar
Enter priority (1 is highest): 2
Enter required computers: 10

Activity 2
Enter activity name: Workshop
Enter priority (1 is highest): 1
Enter required computers: 15

Activity 3
Enter activity name: Presentation
Enter priority (1 is highest): 3
Enter required computers: 8
```

## 6. Sample Output

```
Campus Resource Allocation System

Resource Allocation Results

Activity: Workshop
Allocated: 15
Shortage: 0

Activity: Seminar
Allocated: 5
Shortage: 5

Activity: Presentation
Allocated: 0
Shortage: 8

Remaining computers: 0
```
