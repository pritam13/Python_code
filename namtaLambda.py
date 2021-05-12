def table(n):
 return lambda a:n*a
n=int(input("Please enter your number"))
b=table(n)
for i in range(1,21):
 print(n,"x",i,"=",b(i))
