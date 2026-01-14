##Day 1- 'Hello, World!'

#Day 2: Variables
Create the following variables of different types and print them.
name: String
age: Integer
height: Floating-point number
is_student: Boolean
email: None (representing a null value)
siblings: List
address: Dictionary containing street and city


## Day 3: Input and Output
Basic Input and Output:
Write a program that reads a single input from the user and prints it to the console. For example, if the user enters their name, the program should output: ""Hello, {name}""

Handling Different Data Types:
Extend the program to read and print different types of inputs. Ensure the inputs are properly converted to their respective types and then printed. The program should ask the user to enter:

A string
An integer
A floating-point number

## Day 4: Basic Operators and Expressions
Arithmetic Operators
Write a program to perform the following arithmetic operations using two numbers:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Exponentiation (**)


Relational Operators
Write a program to compare two numbers using the following operators:
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)


Logical Operators
Write a program that evaluates the following between 2 booleans(True or False):
Logical AND (and)
Logical OR (or)
Logical NOT (not)


##Day 5: Conditional Statements and Loops
If-else Statements
Write a program that takes an integer as input and checks if it's even or odd.
Write a program that takes an age as input and determines if the person is a child, teenager, adult, or senior citizen.

Nested If-else Statements
Using nested if-else, write a program that takes three numbers as input and determines the largest among them.

For Loop
Write a program to calculate the sum of all numbers up to the given input number.

While Loop
Write a program to calculate the factorial of a given number.

## Day 6: Funations and Code Reusability
Functions are reusable blocks of code that make programs easier to read, debug, and maintain. Learn how to define, call, and use functions effectively.

Simple Function
Define and call a simple function greet_user which takes name as a parameter. The function should print 'Hello, name' to the console.

Default and Keyword Arguments
Update the greet_user function by adding a default value 'Guest' for the name parameter. When the function is called without an argument it should print 'Hello, Guest' to the console.

Function with Return Values
Write a function that calculates and returns the area of a rectangle. The function should take length and breadth as the arguments.

Variable Scope
To understand the difference between local and global variables, follow these steps:
1. Define a global variable and print its value.
2. Write a function and assign a new value to the same varible inside the function and then print it.
3. Print the variable again outside the function again to observe that its value didn't change.
4. Write another function that access the global variable using the global keyword and then update its value.
5. Print the variable again outside the function. Verify that it's value now got updated.

You'll notice that in step 3, whatever changes made inside the function in step 2 are not reflected but in step 5 when you use the global keyword the variable value gets updated. This shows how the global keyword is used to modify global variables from within a function.
