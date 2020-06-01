class ChaiException(Exception):
    def __init__(self, msg):
        self.__msg = msg


class Chai:
    def __init__(self, temp):
        self.__temp = temp

    def drink_tea(self):
        if self.__temp > 85:
            print("Hot To Drink")
            raise ChaiException("Hot To Drink")
        elif self.__temp < 65:
            print("Cold To Drink")
        else:
            print("Tea Ok to Drink")


try:
    cup = Chai(100)
    cup.drink_tea()
except:
    pass
bobby = Chai(64)
bobby.drink_tea()
