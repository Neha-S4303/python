# If-else Statements
# Write a program that takes an integer as input and checks if it's even or odd.

num = int(input("Enter an integer:", ))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Write a program that takes an age as input and determines if the person is a child, teenager, adult, or senior citizen.
age = int(input("Your age:", ))

if age <= 12:
    print("You're a child")
elif age > 12 and age < 20:
    print("You're a teenager")
elif age >= 20 and age < 60:
    print("You're an adult")
else:
    print("You're a senior")
# Nested If-else Statements
# Using nested if -else , write a program that takes three numbers as input and determines the largest among them.
num_1 = int(input("\n Enter your first numer", ))
num_2 = int(input("\n Enter your second numer", ))
num_3 = int(input("\n Enter your third numer", ))

if num_1 > num_2:
    if num_1 > num_3:
        print("The largest number is", {num_1})
    else:
        print("The largest number is", {num_3})
else:
    if num_2 > num_3:
        print("The largest number is", {num_2})
    else:
        print("The largest number is", {num_3})

# For Loop
# Write a program to calculate the sum of all numbers up to the given input number.
number = int(
    input("\n Enter a positive integer to calculate sum  upto that number :", ))
sum = 0
for n in range(1, number + 1):
    sum += n
print(f" The sum of all the numbers 1 to {number} is {sum}")


# While Loop
# Write a program to calculate the factorial of a given number.
number = int(
    input("\n Enter a number to calculate its factorial :", ))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1
print(f"The Factorial of {number} is {factorial}")
