# Day 23: List intersection
# Write a function to find the intersection of two lists.

def intersection(n, m):
    intersect = []

    for i in n:
        if i in m and i not in intersect:
            intersect.append(i)
    return (intersect)


print(intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
