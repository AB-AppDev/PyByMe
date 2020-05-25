class Excercise:
    global number
    global sum

    def get_input(self):
        self.sum = 0
        self.number = int(input("Enter Number"))
        while self.number != 0:
            self.sum += self.number
            self.number = int(input("Enter Number"))

    def get_sum(self):
        return self.sum


E = Excercise()
E.get_input()
print(E.get_sum())
