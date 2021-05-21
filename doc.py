import flask
def function1(a,b):
          """
          this average is two number of sum
          """
          #docstring
          average=(a+b)/2
          return average
print(function1(10,20))
print(function1.__doc__)