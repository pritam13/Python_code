class Student:
 def __init__(self,name,age,major):
  self.name=name
  self.age=age
  self.major=major

class Arts(Student):
 def __init__(self,name,age,major,sub1,sub2,sub3):
  super().__init__(name,age,major)
  self.sub1=sub1
  self.sub2=sub2
  self.sub3=sub3
 def show(self):
  print("The details of the student",self.name)
  print("The name is",self.name)
  print("The age is",self.age)
  print("The major is",self.major)
  print("The first subject is",self.sub1)
  print("The second subject is",self.sub2)
  print("The third subject is",self.sub3)

st1= Arts("Pritam",30,"Arts","Bengali","Education","Sanskrit")
st1.show()
