# ELSE & FINALLY IN TRY EXCEPT

f1=("jerry.txt")
try:
    f=open("yes.txt")
except Exception as e:
    print(e)
else:
    print("ohh jerry...file is executed")
finally:
    print("i don't care about whatever code at here but i always run-finally ")
f1.close()
