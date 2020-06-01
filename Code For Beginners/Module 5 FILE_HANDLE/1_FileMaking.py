fh = open("example.txt", "w+")
fh.write(input("Enter Info = "))
fh.close()

frd = open("example.txt", "r")
print(frd.read())
frd.close()
