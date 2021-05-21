import flask

j=12 #global varible
def func_1(str):
   j=45 #local variable
   print(j)
   print(str,"hey yarr")
   print(j)
func_1("sun,")
