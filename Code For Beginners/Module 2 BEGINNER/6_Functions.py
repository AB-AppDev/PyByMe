def maxfromtwo(a, b):
    global c
    c = b
    if a > b:
        return a
    else:
        return b


def info(name, roll, *marks):
    print(name, roll, marks)


def info2(name, roll, **marks):
    print(name, roll, marks)


print(maxfromtwo(5, 10))
info("\nAbhi", 2, 70, 60, 65)
info2(name="\nAbhi", roll=2, eng=70, mar=60, hin=65)

print(c)
