def  fiboN(n):
 if n<=1:
  return n
 else:
  return (fiboN(n-1) + fiboN(n-2))

num = int(input("Enter the number to generate the factorial"))
for x in range(1,num+1):
 print(fiboN(x))