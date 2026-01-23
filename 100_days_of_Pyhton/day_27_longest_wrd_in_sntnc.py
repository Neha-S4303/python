# Day 27: Longest word
# Find the longest word in a sentence.

def longestwrd(n):
    dict = {}

    for i in n.split(" "):
        dict[i] = len(i)
    return (max(dict, key=dict.get))


print(longestwrd("This is a sentence is not big"))

# Cleaner Version:


def longest_word(n):
    lngth_ch = 0
    wrd = ""

    for i in n.split(" "):
        if len(i) > lngth_ch:
            lngth_ch = len(i)
            wrd = i

    return (wrd)


print(longest_word("You are beautiful"))
