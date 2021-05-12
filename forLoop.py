set_one = {"India","Denmark","Sweden","Norway","France","Japan","Iceland"}
print(type(set_one))
for x in set_one:
 print(x)

list_one = ["Italy","Greece","Swiss","Austria","Hungary"]
print(type(list_one))
for x in list_one:
 print(x)
else:
 print("The set is finished")

tuple_one = ("India","Denmark","Sweden","Norway","France","Japan","Iceland")
print(type(tuple_one))
for x in list_one:
 print(x)
else:
 print("The tuple is finished")

dic = {"Name" : "Pritam", "Age" : 30, "Address" : "Jaugram"}
print(type(dic))
for x in dic:
 print(x)
else:
 print("The dictionary is finished")

str = "I wanna fuck you"
for x in str:
 print(x)
else:
 print("The string is finished")

for x in range(100):
 if x==21:
  break
 print(x)
else:
 print("The range is finished")

for x in range(3,100,3):
 if x==84:
  continue
 print(x)
else:
 print("The range is finished")

#nested for loop
firstName = ["Pritam","Ruma","Arani","Anam"]
lastName = ["Bhattacharya","Chakrabortty","Banerjee"]
for x in lastName:
 for y in firstName:
  print(y,x)
