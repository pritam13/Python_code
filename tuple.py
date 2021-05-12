mytuple = ("India","Denmark","Sweden","Norway","France","Japan","Iceland")
print(type(mytuple))
print(mytuple)
mylist = list(mytuple)
mylist[3] = "Uruguay"
mytuple = tuple(mylist)
print(mytuple)