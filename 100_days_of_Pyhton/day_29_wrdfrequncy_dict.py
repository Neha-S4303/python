# Words frequency
# Create a dictionary of words and their frequencies.
n = "Here is a sentence and here we are counting the frequency of words in this sentence"
dict = {}

for i in n.split(" "):
    dict[i] = dict.get(i, 0) + 1
print(dict)
