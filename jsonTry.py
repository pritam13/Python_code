import json
#converting text to dictionary
a='{"Name":"Pritam","Age":30,"Address":"Jaugram"}'
b=json.loads(a)
print(b["Name"])
print(b["Age"])

#converting all datatypes to json

c= {
   "name":"Pritam",
   "Age":30,
   "Employes":True,
   "Hobby":("Movies","Sports"),
   "pets":None,
   "Cars":[{"Model":"BMW","mpg":27.6}]}
print(json.dumps(c,indent=5))