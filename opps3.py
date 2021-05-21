#class  Empolyee:
 #   no_of_leaves=5 #class variable
   # def detalis(self):
    #      return f"name of the employee {self.name} & it's salary {self.salary}"

# #jerry = Empolyee() # object
# jerry.name="Jerry"
# jerry.salary='5,00,000'

# print(jerry.detalis())

#--------------------------------------------------------------------------
# constructor- __init__-isme argument bhi pass kar sakte he
class Employee:
    no_of_leaves=5
    @classmethod
    def change_leaves(cls,newleaves):
        # if you change the value of the leaves
        cls.no_of_leaves=newleaves
        harry=Employee()
        # you change the class's properties by object becoz this object are in class method
        harry.change_leaves(10)
        print(harry.no_of_leaves)

    # class method as alternative constructor
    @classmethod
    def str(cls,string):
         pass
         priz=Employee("priz"-'1,00,000')
         print(priz.name)#1,00,000

    @staticmethod
    def good(string):
      print("this is",string)
Employee.good("good")

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     def detalis(self):
#         return f"the name {self.name} & salary {self.salary}"
# jerry=Employee("jerry",'5,00,00,000')
# print(jerry.detalis())
# # print(harry.no_of_leaves)-you can't define the classmethod property outsides

