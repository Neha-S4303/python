# Day 25: Words frequency. Write a function to count the frequency of words in a sentence.

def wrdfrequency(n):
    dict = {}

    for i in n.split(" "):
        dict[i] = dict.get(i, 0) + 1
    for k, v in dict.items():
        print(f"{k} : {v}")
   # return ([dict])


wrdfrequency("how is your day? is your day fun?")
