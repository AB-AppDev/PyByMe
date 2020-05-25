class Temp:
    def __init__(self):
        self.__classData = 100

    def get_classData(self):
        return self.__classData

    def set_classData(self, data):
        self.__classData = data


t = Temp()
print(t.get_classData())

t.set_classData(200)
print(t.get_classData())
