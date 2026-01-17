# Leap Year
# Write a program that checks if a given input year is a leap year or not
# A year is a leap year if:
# it is divisible by 4 and
# not divisible by 100
# unless
# it is also divisible by 400

year = int(input("Year:", ))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, " is not a leap year")
