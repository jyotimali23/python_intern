def calculate_spacing(name, fname, college):
    max_length = max(len(name), len(fname), len(college))
    return max_length

while True:
    try:
        name = input("Enter your name: ")
        fname = input("Enter your Father name: ")
        college = input("Enter your college name: ")
        rnumber = input("Enter your Roll number: ")
        dd = int(input("Enter bdy date: "))
        mm = int(input("Enter bdy month: "))
        yyyy = int(input("Enter bdy year: "))
        dmy = f"{dd}/{mm}/{yyyy}"

        if not name.isalpha() or not fname.isalpha() or not college.isalpha() :
            raise ValueError("Invalid input. Please enter valid details.")

        subject = ["Physics", "MATHS", "CHEMISTRY", "HINDI", "ENGLISH"]
        Marks = []
        Total = []
        grades = []
        MTotal = 0

        for x in subject:
            a = int(input("Enter marks for " + x + ": "))
            if a > 100:
                print("Invalid marks! Please enter marks out of 100.")
                exit(1)
            Marks.append(a)
            MTotal += a
            if a >= 80:
                grades.append("A")
            elif a >= 60:
                grades.append("B")
            elif a >= 40:
                grades.append("C")
            elif a >= 30:
                grades.append("D")
            else:
                grades.append("F")
            Total.append(MTotal)  # Store the total marks for each subject

        max_spacing = calculate_spacing(name, fname, college)
        print("+" + "-" * + "+")
        print("|" + " " * (21 + max_spacing // 2) + "Higher Secondary Education board" + " " * (21 + max_spacing // 2) + "|")
        print("|" + " " * (23 + max_spacing // 2) + "bhopal" + " " * (23 + max_spacing // 2) + "|")
        print("|" + " " * (26 - max_spacing // 2) + "NAME:" + name + " " * (27 - len(name) + max_spacing // 2) + "|", end="")
        print("FATHER NAME:" + fname + " " * (27 - len(fname) + max_spacing // 2) + "|")
        print("|" + " " * (26 - max_spacing // 2) + "COLLEGE:" + college + " " * (27 - len(college) + max_spacing // 2) + "|", end="")
        print("ROLL NUMBER:" + rnumber + " " * (26 - len(rnumber) + max_spacing // 2) + "|")
        print("+" + "-" * (39 + max_spacing) + "+")
        print("|" + " " * (39 + max_spacing) + "|")
        print("| SUBJECTS           MARKS   TOTAL   GRADES |")
        for b2, e, f, g in zip(subject, Marks, Total, grades):
            print("| " + b2 + " " * (31 - len(b2)) + " " + str(e) + " " * (6 - len(str(e))) + " " + str(f) + " " * (6 - len(str(f))) + " " + g + " " * (7 - len(g)) + " |")
        print("+" + "-" * (39 + max_spacing) + "+")
        print("|" + " " * (39 + max_spacing) + "|")
        print("| TOTAL MARKS: {}   | PERCENTAGE: {:.2f}%  |".format(MTotal, (MTotal / 500) * 100))
        print("+" + "-" * (39 + max_spacing) + "+")

        break

    except ValueError as ve:
        print("Error:", ve)