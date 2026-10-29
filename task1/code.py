
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nStudent", i + 1)
    sid = input("Student ID: ")
    name = input("Name: ")
    m1 = float(input("Python marks: "))
    m2 = float(input("Maths marks: "))
    m3 = float(input("English marks: "))

    attendance = float(input("Attendance: "))
    income = float(input("Annual family income: "))

    aggregate = (m1 + m2 + m3) / 3

    if (aggregate >= 75 and m1 >= 60 and m2 >= 60
            and m3 >= 60 and attendance >= 75
            and income <= 250000):

        students.append(
            [sid, name, aggregate, attendance, income]
        )
    else:
        print(name, "is Not Eligible")
students.sort(key=lambda s: (-s[2], -s[3], s[4], s[0]))

print("\nScholarship Rank List")
print("Rank  ID     Name     Aggregate")

for rank, s in enumerate(students, 1):
    print(rank, s[0], s[1], round(s[2], 2))

