
print("Campus Registration ID Analyzer")

sid = input("Enter Student ID: ").upper()

if (len(sid) == 8 and sid[:2].isdigit()
        and sid[2:5].isalpha() and sid[5:].isdigit()):

    year = sid[:2]
    branch = sid[2:5]
    number = sid[5:]

    if branch == "CSE":
        branch_name = "Computer Science"
    elif branch == "ECE":
        branch_name = "Electronics"
    elif branch == "EEE":
        branch_name = "Electrical"
    elif branch == "IT":
        branch_name = "Information Technology"
    else:
        branch_name = "Unknown Branch"

    if branch_name == "Unknown Branch":
        print("Invalid Branch Code")
    else:
        print("Valid Student ID")
        print("Admission Year: 20" + year)
        print("Branch:", branch_name)
        print("Student Number:", number)

else:
    print("Invalid Student ID")

