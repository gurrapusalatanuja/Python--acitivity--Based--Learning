# Campus Registration Identifier Analyzer Using Python

## 1. Problem Statement

 Campus Registration Identifier Analyzer: Examine student identification strings, validate their 
structure, extract specified components, and classify records according to branch and admission year 
codes. 



## 2. Algorithm

1. Start the program.
2. Enter the student registration ID.
3. Check whether the ID contains exactly 8 characters.
4. Check whether the ID has a valid structure.
5. Extract the admission year, branch code, and student number.
6. Identify the student branch.
7. Display the extracted details.
8. Stop the program.

## 3. Flowchart Using Mermaid
```Mermaid
flowchart TD
    A([Start]) --> B[/Enter Student ID/]
    B --> C{ID length is 8?}
    C -- No --> D[Invalid ID]
    C -- Yes --> E[Extract Year Branch and Number]
    E --> F{Valid Branch?}
    F -- No --> D
    F -- Yes --> G[Display Student Details]
    G --> H([Stop])
    D --> H
```



## 5. Sample Input

```
Enter Student ID: 26CSE101
```

## 6. Sample Output

```
Campus Registration ID Analyzer

Valid Student ID
Admission Year: 2026
Branch: Computer Science
Student Number: 101
```
 
