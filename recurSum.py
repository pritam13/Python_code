def  sumN(n):
 if n<=1:
  return n
 else:
  return n+sumN(n-1)

num = int(input("Enter the number until you want the sum"))
print(sumN(num))