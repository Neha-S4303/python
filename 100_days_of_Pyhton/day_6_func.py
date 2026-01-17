# Functions are reusable blocks of code that make programs easier to read, debug, and maintain. Learn how to define, call, and use functions effectively.

# Simple Function
# Define and call a simple function greet_user which takes name as a parameter. The function should print 'Hello, name' to the console.
def greet_user(name):
    print(f"Hello , {name}")


greet_user("Abby")
print()
# Default and Keyword Arguments
# Update the greet_user function by adding a default value 'Guest' for the name parameter.
# When the function is called without an argument it should print 'Hello, Guest' to the console.


def greet_user(name="Guest"):
    print(f"Hello , {name}!")


greet_user()
greet_user("Bobby")

# Function with Return Values
# Write a function that calculates and returns the area of a rectangle. The function should take length and breadth as the arguments.


def calculate_area(length, breadth):

    return (length * breadth)


area = calculate_area(4, 6)
print(f" The area of the rectangle is {area}")

# Variable Scope
# To understand the difference between local and global variables, follow these steps:
# 1. Define a global variable and print its value.
# 2. Write a function and assign a new value to the same varible inside the function and then print it.
# 3. Print the variable again outside the function again to observe that its value didn't change.
# 4. Write another function that access the global variable using the global keyword and then update its value.
# 5. Print the variable again outside the function. Verify that it's value now got updated.
# You'll notice that in step 3, whatever changes made inside the function in step 2 are not reflected but in step 5 when you use the global keyword the variable value gets updated. This shows how the global keyword is used to modify global variables from within a function.

global_var = 10
print(f"The global variable before function call is: {global_var}")


def modify_var():
    global_var = 20
    print(f"Update Global variable inside the function: {global_var}")


modify_var()
print(f"Global variable after function call: {global_var}")


def modify_global_var():
    global global_var  # declare we want to use the global variable
    global_var = 20  # update the global variable
    print(f"Update Global variable inside the function: {global_var}")


modify_global_var()
print(f"Global variable after function call: {global_var}")
