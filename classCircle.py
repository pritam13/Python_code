import math
class circle:
 def __init__(self,radius):
  self.radius = radius
 def calculateArea(self):
  print("The area of the circle is",math.pi*(self.radius**2))
 def calculatePerimeter(self):
  print("The perimeter of the circle is",2*math.pi*self.radius)

choice=''
while choice!='q':
 print("/n/nEnter 1 to calculate area")
 print("Enter 2 to calculate perimeter")
 print("Enter q to quit")
 choice=input("Enter your choice")
 r=int(input("Enter the radius"))
 obj=circle(r)
 if choice=='1':
  obj.calculateArea()
 elif choice=='2':
  obj.calculatePerimeter()
 elif choice=='q':
  print("Thank you for using our function")
  
