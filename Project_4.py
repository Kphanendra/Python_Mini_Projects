# Mini Project 4: Login & User Validation

users = {"phani": "12345678", "user": "abcd"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("*Login Successful! Welcome.", username)
else:
    print("*Invalid Credentials! Please try again.")