 # Mini Project 1: Employee Management System
employees = []

def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter  Age: "))
    role = input("Enter Role: ")
    salary = float(input("Enter Salary: ₹"))
    
    emp = {"Name": name, "Age": age, "Role": role, "Salary": salary}
    employees.append(emp)

def update_employee():
    name = input("Enter Name To Update: ")
    for emp in employees:
        if emp["Name"] ==name:
            print("*** Record Found! Enter New Details***")
            emp["Name"] = input("New Name: ")
            emp["Age"] = int(input("New Age: "))
            emp["Salary"] = float(input("New Salary: "))
            print("***Employee updated successfully.***")
            found = True
            break 
    if not found:
        print("***Employee not found***.")

def delete_employee():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["Name"] == name:
            employees.remove(emp)
            print("***Deleted successfully.***")  
            return
    print("***Employee not found***.")          

def display():
    if not employees:
        print("***No employees in the list.***")
    else:
        for emp in employees:
            print(emp)

while True:
    print("\n1.Add  2.Display  3.Update  4.Delete  5.Exit")
    option = input("Select Any One Option = ")
    if option == "1": add_employee()
    elif option == "2": display()
    elif option == "3": update_employee()
    elif option == "4": delete_employee()
    else: break