import random

upChar = ["A", "B", "C", "E", "D"]
loChar = ["a", "b", "c", "d", "e"]
numChar = [1, 2, 3, 4, 5]
spclChar = ["!", "@", "#", "$", "%"]

wordlist = []
with open("C:\\Users\\abhis\\Desktop\\PyByMe\\simText.txt", "r") as file:
    data = file.readlines()

    for line in data:
        words = line.split()
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())

paswd = random.choice(upChar) + random.choice(loChar) + random.choice(wordlist) + random.choice(loChar) + str(
    random.choice(numChar)) + random.choice(upChar) + random.choice(spclChar) + random.choice(loChar)
print(paswd)


from PyProjects.PasswordGenerate import readable_pass
readable_pass