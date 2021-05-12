#Program to perform mathametical operations

a = int(input("Enter your first number"))
b = int(input("Enter your Second number"))

def sum(arg1,arg2):
 c= a+b
 print("The sum is =",c) 

def sub(arg1,arg2):
 c= a-b
 print("The difference is =",c)

def mul(arg1,arg2):
 return a*b
 

def div(arg1,arg2):
 return a/b
 

sum(a,b)
sub(a,b)
print(mul(a,b))
print(div(a,b))




