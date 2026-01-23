# Day 26: Anagram strings
# Write a function check if two strings are anagrams.

def anagram(a, b):
    first = []
    second = []

    for ch in a:
        first.append(ch)
    for s in b:
        second.append(s)

    return (sorted(first) == sorted(second))


print(anagram("listen", "silent"))


# cleaner version;

def angrm(s, t):
    return (sorted(s) == sorted(t))


print(angrm("earth", "heart"))
