# PALINDROM

#
#
# def palindrom(n, is_palindrom):
#     n = n + 1
#     while not is_palindrom(n):
#       n = n + 1
#     return n
#
# def is_polindrom(n):
#     return str(n) == str(n[::-1])
#
#
# if __name__ == '__main__':
#
#  n = int(input("enter the case type:"))
# numbers  = []
# for i in range(n):
#     i += 1
#     number = int(input(f"enter the number {i} :"))
#     numbers.append(number)
#
# for i in range(n):
#     print(f"the number {numbers[i]} of {palindrom(numbers[i])}")

#----------------another way-----------------------------

def is_palindrom(n):
    n=str(n)
    return str(n)==str(n[::-1])

if __name__ == '__main__':

 ans=int(input("enter the number"))
 if ans is is_palindrom(ans):
     print(f"the number {ans} of {is_palindrom(ans)}")

 elif ans is not is_palindrom():
     ans = ans + 1
     str(ans[0]) == str(ans[2])
     print(f"the number {ans} ")
 else:
     print("enter the valid input")




