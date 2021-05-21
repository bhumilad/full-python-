# abstract method
#
# from abc import ABC , abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         return 0
#
# class Rect(Shape):
#     type="rectangle"
#     sides=4
#
#     def __init__(self):
#         self.length='5'
#         self.breadth='10'
#
#     def area(self):
#         return self.length*self.breadth
#
# r= Rect()
# print(r.area())

print("___________________________________________________________________________________________")

#setter & property decoraters
#
# class Employee:
#
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         self.email=f"{fname}{lname}@gmail.com"
#
#     def detalis(self):
#         return f" the employee is {self.fname} {self.lname}"
#
#     def email(self):
#         pass
#
# emp=Employee("jerry","lad")
# print(emp.email)
# print(emp.detalis())
