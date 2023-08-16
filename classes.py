class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age=age
        self.position = position
        self.salary = salary
        self._annual_salary= None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        
        return self.salary

    @salary.setter
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary
        self._annual_salary= None

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)}) "
        )
    
    @property
    def salary(self):
        return self._salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary=self.salary * 12
        return self._annual_salary
         

employee1= Employee("Diana", 22, "developer", 1200)
employee2= Employee("Bogdan", 32, "tester", 1000)
print(employee1)