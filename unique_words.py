import requests

link1 = "https://www.gutenberg.org/cache/epub/11/pg11.txt" #Alice in Wonderland
punctuation = ",.?!';\"-=:()"
book1 = requests.get(link1)

unique_words1 = {}
lines = book1.text.splitlines()
def dictionary1():
    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            word = word.lower()
            if len(word) > 4:
                unique_words1[word] = unique_words1.get(word, 0) + 1
dictionary1()

link2 = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt" #The Great Gatsby
punctuation = ",.?!';\"-=:()"
book2 = requests.get(link2)

unique_words2 = {}
lines = book2.text.splitlines()
def dictionary2():
    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            word = word.lower()
            if len(word) > 4:
                unique_words2[word] = unique_words2.get(word, 0) + 1
dictionary2()

print(len(unique_words1))
print(len(unique_words2))