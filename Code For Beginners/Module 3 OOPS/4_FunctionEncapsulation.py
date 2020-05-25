class Temp:
    def __init__(self):
        self.__classData = 100

    def get_classData(self):
        return self.__classData

    def set_classData(self, data):
        self.__classData = data

    def __private_setData(self, data):
        self.__classData = data
        return self.__classData


t = Temp()
print(t.get_classData())

t.set_classData(200)
print(t.get_classData())

# accessing __private_setData
#print(t.__private_setData())
