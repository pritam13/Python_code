dic1 = {"Name" : "Pritam", "Age" : 30, "Address" : "Jaugram"}
print(dic1)
print("Name is", dic1["Name"])
print("Age is", dic1.get("Age"))
dic1["Age"] = 25
print("Updated Age is", dic1.get("Age"))
dic1["Salary"] = 59000
print("The length is",len(dic1))
print(dic1)
dic1.pop("Address")
print(dic1)
dic1.popitem()
print(dic1)
dic2 = dic1.copy()
print(dic2)