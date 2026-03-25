# Mini Project 6: String Formatter Tool

name = input("Enter name: ")
product = input("Enter product: ")

print(f"\nResult: {name} bought {product}")

print("\n----- Alignment  -----")
print(f"Left:   |{name.ljust(15)}|")
print(f"Right:  |{name.rjust(15)}|")
print(f"Center: |{name.center(15)}|")
