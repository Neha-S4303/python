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

## Day 7: Lists and Tuples
Lists
Lists are one of the most commonly used data structures in Python. They are ordered and mutable, which means you can change their content after creation. Lists can store any type of data - strings, numbers, or even other lists. This makes them powerful and flexible for a wide range of tasks.

Create a List: Start by creating a list with 5 elements. These could be fruits, numbers, or a mix of data types.
Access Elements: Use both positive and negative indices to retrieve items from the list.
Modify the List: Learn how to append, insert, remove, or update elements using built-in methods.
Slice the List: Use slicing to create sublists by selecting a specific range of elements.
Iterate Through the List: Use loops (like for or while) to go through each item and perform operations on them.
Tuples
Tuples are also ordered collections, just like lists, but with one key difference - they are immutable. Once a tuple is created, you can't change its content. Tuples are ideal when you want to store data that should not be altered, like coordinates, configuration settings, or fixed values.

Create a Tuple: Define a tuple containing different types of data, such as strings, numbers, or booleans.
Access Elements: Retrieve elements using index positions, just like you would with a list.
Tuple Operations: Perform operations like concatenation (+) and repetition (*), or check membership with in.
Convert to a List: If you need to modify the tuple, convert it into a list, make the changes, and convert it back if needed.

## Day 8- Sets and Dictionaries

Sets
Sets are unordered collections of unique elements. They are useful when you want to eliminate duplicates and perform common set operations like union, intersection, and difference. Since sets are unordered, items do not have a fixed position and cannot be accessed using an index.

Create a Set: Define a set with multiple elements, including duplicates, and observe how duplicates are automatically removed.
Add and Remove Items: Use add() to insert elements and remove() or discard() to delete them.
Set Operations: Learn how to perform mathematical set operations like union(), intersection(), and difference().
Loop Through a Set: Use a loop to iterate over the elements in a set.
Dictionary
Dictionaries are unordered collections of key-value pairs. They allow you to associate a unique key with a value, making them ideal for looking up data efficiently. Keys must be unique and immutable, while values can be of any type.

Create a Dictionary: Define a dictionary with keys and corresponding values (e.g., name-age pairs).
Access Values: Use a key to retrieve the associated value using square brackets or the get() method.
Update and Add Items: Modify existing key-value pairs or add new ones.
Remove Items: Use methods like pop() or del to remove entries from the dictionary.
Loop Through a Dictionary: Iterate through keys, values, or both using a for loop with .items(), .keys(), or .values().

## Day 9: Random number generator
1. Write a program that generates a random number. 
2. Write a program that generates random number between 2 integers

## Day 10: For-loop
Use a for loop to print numbers from 1 to 10.

## Day 11: While-loop
Use a while loop to print even numbers from 2 to 20.

## Day 12: Odd-even
Write a program to check if a number is even or odd.

## Day 13: Largest of three numbers.
Write a program to find the largest of three numbers.

## Day 14: Leap Year
Write a program that checks if a given input year is a leap year or not

## Day 15: Factorial
Write a function to calculate the factorial of a number.

## Day 16: Palindrome String
Write a function to check if a given string is a palindrome.

## Day 17:  Number of vowels in a string
Write a function to count the number of vowels in a string.

## Day 18: List Sum
Write a function to find the sum of all elements in a list.

## Day 19: Maximum in List
Write a function to find the maximum element in a list.

