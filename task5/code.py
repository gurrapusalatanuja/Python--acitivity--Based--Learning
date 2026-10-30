n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    row = []
    print("Enter marks of Student", i + 1)

    for j in range(m):
        mark = int(input("Enter subject mark: "))
        row.append(mark)

    marks.append(row)

# Row-wise total and average
print("\nStudent Total and Average")

averages = []

for i in range(n):
    total = sum(marks[i])
    avg = total / m
    averages.append(avg)

    print("Student", i + 1, "Total:", total,
          "Average:", round(avg, 2))

# Column-wise average
print("\nSubject Averages")

for j in range(m):
    total = 0

    for i in range(n):
        total += marks[i][j]

    avg = total / n
    print("Subject", j + 1, "Average:", round(avg, 2))

    if avg < 50:
        print("Low Performance Subject")

# Top performer
top = averages.index(max(averages))

print("\nTop Performer: Student", top + 1)
print("Highest Average:", round(averages[top], 2))
