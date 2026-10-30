# Student Marks Matrix Analysis Using Python

## 1. Problem Statement

Develop a simple Python program to analyze student marks stored in a matrix. The program calculates each student's total and average marks, calculates subject-wise averages, identifies the top-performing student, and detects subjects with low average performance.

## 2. Algorithm

1. Start the program.
2. Enter the number of students and subjects.
3. Enter the marks of each student.
4. Store the marks in a matrix.
5. Calculate each student's total and average marks (row-wise).
6. Calculate each subject's average marks (column-wise).
7. Identify the student with the highest average.
8. Identify subjects with an average below 50.
9. Display all results.
10. Stop the program.

## 3. Flowchart Using Mermaid

flowchart TD
    A([Start]) --> B[/Enter students and subjects/]
    B --> C[/Enter marks matrix/]
    C --> D[Calculate student totals and averages]
    D --> E[Calculate subject averages]
    E --> F[Find top student]
    F --> G[Find subjects with low average]
    G --> H[Display results]
    H --> I([Stop])



## 5. Sample Input

```
Enter number of students: 3
Enter number of subjects: 3

Enter marks of Student 1
80
90
70

Enter marks of Student 2
60
50
40

Enter marks of Student 3
90
85
95
```

## 6. Sample Output

```
Student Marks Matrix Analysis

Student Total and Average

Student 1 Total: 240 Average: 80.0
Student 2 Total: 150 Average: 50.0
Student 3 Total: 270 Average: 90.0

Subject Averages

Subject 1 Average: 76.67
Subject 2 Average: 75.0
Subject 3 Average: 68.33

Top Performer: Student 3
Highest Average: 90.0
```

