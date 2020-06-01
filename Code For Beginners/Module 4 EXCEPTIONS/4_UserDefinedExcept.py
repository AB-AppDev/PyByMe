class Chai:
    def __init__(self, temp):
        self.__temp = temp

    def drink_tea(self):
        if self.__temp > 85:
            print("Hot To Drink")
            raise ValueError("Hot To Drink")
        elif self.__temp < 65:
            print("Cold To Drink")
        else:
            print("Tea Ok to Drink")


cup = Chai(100)
cup.drink_tea()
