class parent:
    def __init__(self, name):
        print("Parent")

class child(parent):
    def __init__(self):
        print("Child")
        super().__init__("Hello")

C = child()
print(child.__mro__)