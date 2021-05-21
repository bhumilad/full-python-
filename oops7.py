# public ,private & protected Access specifiers

class Employee:
    no_of_project=9
    _protected=9
    __private=98

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def detalis(self):
        return f"this is name of the employee {self.name} and the salary {self.salary}"

person=Employee("jerry",'8,00,000')
print(person._protected)

print(person._Employee__private) # for private you are writing like this