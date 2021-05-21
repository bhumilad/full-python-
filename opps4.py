# single inheritance

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detalis(self):
        return f"this is name of the employee {self.name} and the salary {self.salary}"

class Programmer(Employee):
    def __init__(self,name,salary,languages):
        self.name = name
        self.languages = languages
        self.salary=salary

    def prog(self):
        return f"this is name of the programmer {self.name} , salary is {self.salary} and the languages {self.languages}"

jerry = Employee("jerry", '8,00,000')
print(jerry.detalis())

#inherite the class
lerry=Programmer("lerry",'1,00,000',["python","c"])
print(lerry.detalis()) # this is name of the employee lerry and the salary 1,00,000
print(lerry.prog()) # this is name of the programmer lerry , salary is 1,00,000 and the languages ['python', 'c']

