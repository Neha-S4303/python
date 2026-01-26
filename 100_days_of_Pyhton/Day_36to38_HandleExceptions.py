# Day 36: Handle Exceptions:
# Handle exceptions for division by zero.

try:
    x = int(input("Enter numerator", ))
    y = int(input("Enter denominator", ))
    print(" Answer:", x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Day 37: Handle Exceptions II
# Handle exceptions for file not found.

try:
    with open("doesntexist.txt", "r") as d:
        contents = d.read()
        print(contents)
except FileNotFoundError:
    print("File doesn't exist")

# Day 38: Custom Exceptions:
# Create a custom exception class.
