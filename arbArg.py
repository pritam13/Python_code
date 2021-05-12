#Program for arbitrary argument
a = int(input("Enter your first number"))
b = int(input("Enter your Second number"))


def sum(*arg):
  c=arg[0]+arg[1]
  print("The sum is =",c) 

def sub(**arg):
 c= arg["arg1"]-arg["arg2"]
 print("The difference is =",c)

def mul(arg1,arg2):
 c= a*b
 print("The multiplication is =",c)

def div(arg1,arg2):
 c= a/b
 print("The division is =",c)

sum(a,b)
sub(arg1=a,arg2=b)
mul(a,b)
div(a,b)




