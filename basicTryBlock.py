#Normal try block
try:
 print(x)
except NameError:
 print("Variable X is not defined")
except:
 print("Unknown Error")

#try block with else
try:
 print("welcome")
except NameError:
 print("Variable X is not defined")
else:
 print("Everything is fine")

#try block with finally

try:
 print("Finally check")
except:
 print("Variable X is not defined")
finally:
 print("The try and the except block is finished")