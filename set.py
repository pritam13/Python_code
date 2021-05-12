set_one = {"India","Denmark","Sweden","Norway","France","Japan","Iceland"}
set_two = {"Italy","Greece","Swiss","Austria","Hungary"}
print(type(set_one))
print(set_one)
print(set_two)
set_one.add("Pakistan")
set_two.update(["China","Ghana", "Africa"])
print(set_one)
print(set_two)
set_three = set_one.union(set_two)
print(set_three)
set_three.discard("Pakistan")
print(set_three)