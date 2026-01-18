# Write a function to check if a given string is a palindrome.


def IsPalindrom(s):
    s = "".join(ch.lower() for ch in s if ch.isalnum())

    return s == s[::-1]


print("Is Palindrome", IsPalindrom("Was it a car or a cat I saw?"))
