fh = open("words2.txt", "r")
list = fh.read().replace(",", " ").split()
print(len(list))
