# join,map,filter & reduce:
from shlex import join

#1.join func
lis2=["ronny","siya","jerry","priz","mom-dad","bhau"]
# a= print(join(lis2),"shivi",sep=',')

#2.map func
# num=["35","45","55"]
# num=list(map(int,num))
# num[1]=num[1]+5
# print(num[1])
print("------")

num=[3,4,5]
print(list(map(lambda a:a*a,num)))
print("------")

 # def square(a):
 #   return a*a
# def cube(a):
 #   return a*a*a
# function=[square,cube]
# for item in range(5):
# print(list(map(lambda x:x(item),function)))

#3.filter func
list_1=[1,2,3,4,5,6,7,8,9,10,11,23,12,21]
def less_5(n):
    return n>5
print(list(filter(less_5 , list_1)))

#4.reduce func
from functools import reduce
listt=[1,2,3,4]
print(reduce(lambda a,b:a+b,listt))

