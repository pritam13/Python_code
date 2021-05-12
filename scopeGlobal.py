x=400
print("Outside show",x)
def show():
 global x
 x=300
 print("Inside show, change value",x)
show()
print("Outside show",x)