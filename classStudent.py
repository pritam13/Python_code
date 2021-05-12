class student:
 def __init__(self,name,age,major):
  self.name=name
  self.age=age
  self.major=major

 def show(self):
  print("The details of the student",self.name)
  print("The name is",self.name)
  print("The age is",self.age)
  print("The major is",self.major)

st1= student("Pritam",30,"Science")
st1.show()
st2= student("Arani",32,"Arts")
st2.show()
st3= student("Anam",37,"Commerce")
st3.show()
st2.show()