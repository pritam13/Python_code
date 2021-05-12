list_one = ["India","Denmark","Sweden","Norway","France","Japan","Iceland"]
list_two = ["Italy","Greece","Swiss","Austria","Hungary"]
print(list_one)
print(list_two)
print("Print item 2 to 5", list_one[2:5])
print("Print item up to 5", list_one[:5])
print("Print item from 3", list_one[2:])
print("Print item up to -5", list_one[:-5])
print("Print item from -3", list_one[-3:])
list_one.append("Greenland")
list_two.insert(3,"Australia")
print(list_one)
print(list_two)
list_three = list_one + list_two
print(list_three,len(list_three))
list_three.remove("Japan")
print(list_three,len(list_three))
list_three.clear()
print(list_three,len(list_three))