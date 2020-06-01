a = 10
b = 20
print(a + b)

p = "Hello"
q = "World"
print(p + q)

x = [10, 20, 30]
y = [5, 6, 7]
print(x + y)


class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __gt__(self, other):
        return self.pages > other.pages;


javabook = Books(100)
pythonbook = Books(150)

print(javabook.__add__(pythonbook))
print(pythonbook.__gt__(javabook))
