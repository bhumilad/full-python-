f=open("jerry.txt")
print(f.readline())
f.seek(2)
print(f.readline())
f.close()

with open("jerry.text")as f:
    print(f.readline())