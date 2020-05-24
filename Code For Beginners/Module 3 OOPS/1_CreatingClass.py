class Student:
    def __init__(self):
        self.name = "Abhishek"
        self.age = 20
        self.marks = 75

    def talk(self):
        print("Name = ", self.name)
        print("Age  = ", self.age)
        print("Marks = ", self.marks)

Obj = Student()

print(Obj.name)
Obj.name = "Abhi"

print(Obj.talk())
