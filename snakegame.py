#snack water gun
import random
chance=0
c=0
i=0
print("s=snack\nw=water\ng=gun")
print("your turn:")
i=input()
print("computer turn:")
lis =['s','w','g']
c=random.choice(lis)
print(c)
#you have 10 chance
while chance<10:
    if i==c:
        print("oh same")
        print("both have 0&0")
        break
    elif i>c:
        i='s'
        c='w'
        print("computer won")
        c+=1
    elif i<c:
        i='w'
        c='s'
        print("oh!you win")
        i+=1
    elif i<c:
        i='g'
        c='s'
        print("oh!you win")
        i+=1
    elif i>c:
        i ='g'
        c ='s'
        print("computer won")
        c += 1
    elif i<c:
        i='g'
        c='w'
        print("oh!you win")
        i+=1
    else:
        i='w'
        c='g'
        print("computer won")
        c+=1



