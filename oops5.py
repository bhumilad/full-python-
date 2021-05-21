#mltiple inheritance

class Employee:
    no_of_project=9

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detalis(self):
        return f"this is name of the employee {self.name} and the salary {self.salary}"

class Programmer:
    #no_of_project=8

    def __init__(self,name,salary,languages):
        self.name = name
        self.languages = languages
        self.salary=salary

    def detalis(self):
        return f"this is name of the programmer {self.name} , salary is {self.salary} and the languages {self.languages}"

class Coder(Employee,Programmer):
    # no_of_project=7

    def __init__(self, name, salary, languages, role):
            self.name = name
            self.salary = salary
            self.languages = languages
            self.role = role

    def code(self):
            return f"this is name of the programmer {self.name} , salary is {self.salary} , " \
                   f"the languages {self.languages} & the role - {self.role}"

person=Coder("person",'1,00,000',["python","c"],"web devolper")
# coder class inherit 1st Employee class.so print below
print(person.detalis())
# comment the no_of_project in Coder
print(person.no_of_project) # 9