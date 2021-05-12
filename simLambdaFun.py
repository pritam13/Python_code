x=lambda a:a+10
print(x(25))

def square(a):
 return lambda b:a*b
y= square(5)
print(y(8))