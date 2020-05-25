n = input("Name: ")
a = int(input("Age: "))
m = int(input("Marks: "))


class Student:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("\nHi ", self.name, ",")
        print("Your Age is ", self.age)
        print("Your Marks is ", self.marks)


s1 = Student(n, a, m)
s2 = Student("RPB", 18, 85)
s1.display()
s2.display()
