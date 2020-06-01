class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def ann_salary(self):
        return (self.pay * 12) + self.reward


class Employee:
    def __init__(self, position, name, sal):
        self.name = name
        self.position = position
        self.finSalary = sal

    def callSalary(self):
        return self.finSalary.ann_salary()


sal = Salary(100000, 10000)
emp = Employee("Abhi", "Py Dev", sal)

print(emp.callSalary())
