import random

upChar = ["A", "B", "C", "E", "D"]
loChar = ["a", "b", "c", "d", "e"]
numChar = [1, 2, 3, 4, 5]
spclChar = ["!", "@", "#", "$", "%"]

passwd = random.choice(upChar) + random.choice(upChar) + random.choice(loChar) + str(
    random.choice(numChar)) + random.choice(spclChar) + random.choice(loChar) + str(
    random.choice(numChar)) + random.choice(spclChar)

print(passwd)
