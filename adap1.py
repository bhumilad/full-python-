n=int(input("n:"))
count=0
m=0
# for i in range (n):
#     count=count+i
#     for j in range(n):
#         count=count+j
#         for k in range(n):
#             count=count+k
# print("step of i",i+1)
# print("step of j",j+1)
# print("step of k",k+1)
# print("total step of count",count)

for i in range (n):
    count=count+1
    m=m+i
print("step of i",i+1)
print("step of m",m+1)
print("total step of count",count)
