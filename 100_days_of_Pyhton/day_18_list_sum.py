# List sum
# Write a function to find the sum of all elements in a list.

def List_sum(n):

    total = 0
    for i in n:
        total += i
    return total


print(List_sum([1, 2, 3, 4, 5]))
