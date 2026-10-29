
import math
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
threshold = float(input("Enter required attendance percentage: "))
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
elif not 0 < threshold <= 100:
    print("Invalid attendance threshold")
else:
    current = (attended / total) * 100
     print("Current attendance:", round(current, 2), "%")
   if current >= threshold:
        print("Attendance requirement already satisfied")
        print("Additional classes required: 0")
    else:
        required = math.ceil(
            (threshold * total - 100 * attended)
            / (100 - threshold)
        )

        print("Minimum consecutive classes to attend:", required)

        new_percentage = (
            (attended + required) / (total + required)
        ) * 100

        print("Attendance after recovery:", round(new_percentage, 2), "%")


