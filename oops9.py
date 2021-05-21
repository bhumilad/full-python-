# operater overloading & dunder method-the start from __ & end with __ =imp

class Employee:
    no_of_project=9

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detalis(self):
        return f"this is name of the employee {self.name} and the salary {self.salary}"

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return f"name {self.name},,,,salary {self.salary}"

    def __str__(self):
        return f"string ...{self.name},,{self.salary}"

emp1=Employee("elon",150)
emp2=Employee("musk",150)
print(emp1+emp2)

# this is call overloading
print(emp1)# str>repr-as ex
# string ...elon,,150
# if you want to repr than you can give specific
print(repr(emp1))# name elon,,,,salary 150




