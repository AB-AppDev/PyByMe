""" * Creating A List - []"""

myList = [2, "Abhishek Bhalerao", "84xxx424xx"]
print(myList)
print(myList[2])
print()

""" * Creating A tuple - ()"""

myTuple = (2, "Abhishek Bhalerao", "84xxx424xx")
print(myTuple[0])
print()
"""
No outside indexing Allowded

>print(myTuple[3])

Line Generating err - 
    print(myTuple[3])
IndexError: tuple index out of range
"""

""" * Creating A Range"""

'''Print 1to9'''
rng = range(1, 10)
q = list(rng)
print(q)

'''OddNums'''
rng = range(1, 10, 2)
q = list(rng)
print(q)

'''EvenNums'''
rng = range(2, 10, 2)
q = list(rng)
print(q)

"""
No outside indexing Allowded

>print(myTuple[3])

Line Generating err - 
    print(myTuple[3])
IndexError: tuple index out of range
"""
print()

