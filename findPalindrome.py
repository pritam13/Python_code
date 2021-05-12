# Find palindrome number until given number

def palindromeUntil(num1):
 i = 1
 while i!=num1:
  b=i
  sum=0
  while i!=0:
   r=i%10
   sum=sum*10+r
   i=int(i/10)
  if sum==b:
   print(b)
   i=b+1
  else:
   i=b+1

num1 = int(input("Please enter the limit until you want to search palindrome"))
palindromeUntil(num1)