fh = open("example.txt", "w")

for i in range(1, 11):
    fh.write("%d\n" % i)

fh.close()
