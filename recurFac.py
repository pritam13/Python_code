def  facN(n):
 if n<=1:
  return n
 else:
  return n*facN(n-1)

num = int(input("Enter the number to generate the factorial"))
print(facN(num))