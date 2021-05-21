#multilevel inheritance

class Employee:
    no_of_project=9

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detalis(self):
        return f"this is name of the employee {self.name} and the salary {self.salary}"

class Programmer(Employee):
    #no_of_project=8

    def __init__(self,name,salary,languages):
        self.name = name
        self.languages = languages
        self.salary=salary

    def prog(self):
        return f"this is name of the programmer {self.name} , salary is {self.salary} and the languages {self.languages}"

class Coder(Programmer):
   # no_of_project=7

    def __init__(self,name,salary,languages,role):
        self.name = name
        self.languages = languages
        self.salary=salary
        self.role=role

    def code(self):
        return f"this is name of the programmer {self.name} , salary is {self.salary} , " \
               f"the languages {self.languages} & the role - {self.role}"

person1=Coder("person1",'1,00,000',["python","c "],"web devolper")
print(person1.detalis())
print(person1.prog())
print(person1.code())

# print(person1.no_of_project) # 7

# if you comment out no_of_project in coder class
# print(person1.no_of_project) # 8

# if you comment out no_of_project in programmer class
print(person1.no_of_project) # 9





