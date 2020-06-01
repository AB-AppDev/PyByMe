class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def ann_salary(self):
        return (self.pay * 12) + self.reward


class Employee:
    def __init__(self, position, name, pay, reward):
        self.name = name
        self.position = position
        self.finSalary = Salary(pay, reward)

    def callSalary(self):
        return self.finSalary.ann_salary()


emp = Employee("Abhi", "Py Dev", 100000, 10000)

print(emp.callSalary())
