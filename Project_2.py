# Mini Project 2: Student Report Card

def report():
    name = input("Enter name: ")
    Matchs = int(input("Matchs: "))
    Since = int(input("Since: "))
    English = int(input("English: "))

    total = Matchs + Since + English
    avg = total / 3

    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 50:
        grade = "B"
    elif avg >= 35:
        grade = "c"
    else:
        grade = "D"
    
    print("-" * 15)
    print(f"REPORT CARD")
    print("-" * 15)
    print(f"Name:    {name}")
    print(f"Total:   {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade:   {grade}")
    print("-" * 15)

report()