# Mini Project 5: Unique Visitor Counter

# 1. Store visitor names in a set
visitors = set()

print("* Visitor Tracking System *")
print("(Type 'stop' to finish)")

while True:
    name = input("Enter visitor name: ").strip().lower()
    
    if name == "stop":
        break
    
    if name:
        visitors.add(name)

print("-" * 25)
print("Total Unique Visitors: ", len(visitors))
print("Visitor List:", "," .join(visitors).title())