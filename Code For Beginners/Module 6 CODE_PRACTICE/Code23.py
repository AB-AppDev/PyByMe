fh = open("word.txt","r")
words = fh.read().split()
print(len(words))