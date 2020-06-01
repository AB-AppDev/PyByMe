fh = open("example.txt", "w+")
fh.write(input("Enter Info = "))
fh.close()

fr = open("example.txt", "r")
print(fr.read())
fr.close()
