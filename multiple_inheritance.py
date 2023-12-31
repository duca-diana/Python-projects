class Employee:
    __slots__=("name", "age", "salary", )
    def __init__(self, name, age, salary):
        self.name = name
        self.age=age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class SlotsInspectorMixin:
    __slots__= ()
    def has_slots(self):
        return hasattr(self, "__slots__")

class Developer(SlotsInspectorMixin, Employee):
    __slots__=("framework", )
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

    

employee2= Developer("Diana", 22, 1000)

employee2.increase_salary(20, 30)
print(employee2.salary)