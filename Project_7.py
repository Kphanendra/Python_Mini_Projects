# Mini Project 7: Bank Account System

account = {"name": "", "balance": 0}

def create():
    account["name"] = input("Enter name: ")
    account["balance"] = float(input("Enter balance: "))

def deposit():
    amt = float(input("Amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

def check():
    print("Balance:", account["balance"])

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit")
    option = input("Choice option: ")
    if option == "1": create()
    elif option == "2": deposit()
    elif option == "3": withdraw()
    elif option == "4": check()
    elif option == "5": break
    else: print("Invalid")
    