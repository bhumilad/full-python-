# class variable & instance

class Empolyee:
    no_of_leaves=5 #class variable
    # pass
jerry=Empolyee() # object
siya=Empolyee() # object
ronny=Empolyee() # object

# jerry employee
jerry.name="Jarry"
jerry.no=18
jerry.salary=5,00,000

# siya employee
siya.name="Siya"
siya.no=1
siya.salary=10,00,000

# ronny employee
ronny.name="Ronny"
ronny.no=18
ronny.salary=15,00,000

print(jerry.no_of_leaves)

# if you change the class variable
Empolyee.no_of_leaves=8

print(jerry.no_of_leaves)

