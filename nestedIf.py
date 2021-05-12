num1 = int(input("Enter your first number"))
if num1>30:
 print(num1,"is the greater than 30")
 if num1<60:
  print(num1,"is the lesser than 60")
 else:
  print(num1,"is the greater than 60")
else:
 print(num1,"is lesser than 30") 
num2 = int(input("Enter your second number"))
if num2>num1:
 pass
else:
 print(num2,"is the lesser than",num1)