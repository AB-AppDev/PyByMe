fh = open("example.txt", "w")

for i in range(1, 11):
    fh.write("%d\n" % i)
fh.close()

fh = open("example.txt", "r")
print(fh.read(5))
print(fh.readline(6))
fh.close()
