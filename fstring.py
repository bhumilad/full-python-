#string formatting
print("1st example...")
me="jerry"
a="this is %s" %me
print(a)
print("-----------------------------------------------------")

print("2nd example....")
me="jerry"
a1=18
print("this is %s%s"%(me,a1))
print("-----------------------------------------------------")

#.format()
print("example of .formatting")
a="jerry"
b=18
me="this is {}{}"
i=me.format(a,b)
print(i)
print("-----------------------------------------------------")

print("string formatting in other type")
a="jerry"
b="lad"
c="this is {0} {1}"
me=c.format(a,b)
print(me)

print("-----fstring------")
#--------Fstring----------

a="elon" #input()
b="musk" #input()
me=f"this is {a} {b}.this man is legend"
print(me)
print("-----------")
import random
lis=["jerry","herry","merry","lerry"]
my=f"this {random.choice(lis)}"
print(my)
print(type(lis))