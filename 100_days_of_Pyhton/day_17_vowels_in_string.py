# Number of vowels in a string
# Write a function to count the number of vowels in a string.

def Vowel(s: str):
    v = ""

    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u']:
            v += ch
    return (len(v))


print(Vowel("supercalifragilisticexpialidocious"))
