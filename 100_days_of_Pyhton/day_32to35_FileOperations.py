# Day 32: File operations: Read
# Read and display the contents of a text file.

# using with, you don't need to close using with
with open("C:/Users/nhshe/OneDrive/Desktop/makeovermonday-2023w40/Make over monday/paid leave by country.csv", "r") as f:
 # the file path has back slash "\" which gives unicode error, so changed it to forward slash python accepts it
    contents = f.read()

    print(contents)

# Day 33: File operations: Write
# Write data to a text file.

with open("output.txt", "w") as f:
    # "w"Creates the file if it doesn’t exist, replaces everything if it does.
    f.write("Hello Neha \n")
    f.write("This is Day 33 of Python 100daysofcode \n")

with open("output.txt", "r") as d:
    contents = d.read()
    print(contents)

# Day 34: File operations: Append
# Append data to an existing text file.

with open("output.txt", "a") as f:
    # "a"Adds new content at the end without deleting existing text.
    f.write("This is Day 34 and I'm adding a new line \n")

with open("output.txt", "r") as d:
    contents = d.read()
    print(contents)

# Day 35: File operations:
# Calculate the average of numbers in a text file.

import csv


def average_column(filename, columnname):
    value = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            value.append(float(row[columnname]))
        return (sum(value)/len(value))


print(average_column("C:/Users/nhshe/OneDrive/Desktop/makeovermonday-2023w40/Make over monday/paid leave by country.csv", "Paid Leave Days"))
