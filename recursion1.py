#recursions in two type:-1.iterative approach
#                        -2.recursive approach
#1 .....
"""
i=0
def iter_app(a):
        for i in range(a):
           fac=1
           fac=fac*(i+1)
           return fac
           i+=1

number=int(input("enter the num:"))
print(iter_app(number))
"""
#2 ....
from math import factorial


def rec_1(n):
    if(n==1):
        return 1
    else:
        return n * factorial(n-1)
number= int(input("enter the number:"))
print(rec_1(number))
