# Reverse words in a sentence.

def Reverse_Sen(n):
    word_list = []

    for i in n.split(" "):
        word_list.insert(0, i)

    return (" ".join(word_list))


print(Reverse_Sen("this is a sentence"))
