# *args & *kwargs


print("-----*args-----")
def funcargs(*args):
  for item in args:
         print(item)
lis=["jerry","koko","elon","mark","bill"]
n="my frd:"
funcargs(n,*lis)

print("------*kwargs-------")
def funkargs(**kwargs):
    print("person:")
    for key,value in kwargs.items():
        print(f"this person {key} for me - {value}")
        nor="always"
kw={"akky":"mean","siya":"my girl","ronny":"cutee","priz":"bff"}
funkargs(**kw)


