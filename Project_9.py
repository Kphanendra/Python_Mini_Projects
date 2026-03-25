# Mini Project 9: Course Enrollment System

students = {}

def add_student():
    name = input("Name: ")
    courses = input("Courses (comma separated): ").split(",")
    students[name] = courses

def update():
    name = input("Name: ")
    if name in students:
        students[name] = input("New courses: ").split(",")

def display():
    print(students)

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    option = input("Choice option: ")
    if option == "1": add_student()
    elif option == "2": update()
    elif option == "3": display()
    elif option == "4": break
    else: print("Invalid choice, try again.")