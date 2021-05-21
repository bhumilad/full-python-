# comprehension in python

li = []
for i in range(100):
    if i % 3 == 0:
      li . append(i)
print(li)

# in above program ,if you have to apply comprehension

li=[i for i in range(100) if i % 3 == 0]
print(li)

#
# i=1
# dict1={i:f" item {i}" for i in range (5)}
# print(dict1)
# # dict={value:key for key , value in dict1.item()}
# # print(dict)
# print(type(dict1))

print("---------------------------------------------------------")

# generator in python -yield is also generator
# yield function - on the fly generate karta he value ko

def gen(n):
    for i in range(n):
        yield i
g=gen(133)
print(g) #<generator object gen at 0x011755A0>

print("___________________ITERABLE___________________")
# string is iterable
h="jerry"
for i in  (h):
    print(i)
print(iter(h))
c=iter(h)
print(c.__next__())
print(c.__next__())
print(c.__next__())






