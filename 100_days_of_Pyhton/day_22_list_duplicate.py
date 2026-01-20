# Day 22: List duplicates
# Write a function to remove duplicates from a list.

def RemoveDups(r):
    newlist = []

    for i in r:
        if i not in newlist:
            newlist.append(i)

    return (newlist)


print(RemoveDups([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
