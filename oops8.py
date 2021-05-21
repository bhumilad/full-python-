# overriding and super()

class A:
    var1="i am in class A"

    def __init__(self):
        self.var1="i am in inside class A"
        self.instance="i am instance of class A"

class B(A):
    var2 ="i am in class B"

    def __init__(self):
        self.var1 = "i am in inside class B"
        # self.instance = "i am instance of class B"
        # super.__init__()
# object
a=A()
b=B()
super.__init__()


print(a.var1) # i am in inside class A
print(b.var1) # i am in inside class B

# if i comment the var1 & instance in class B than below
print(b.var1) # i am in class A









