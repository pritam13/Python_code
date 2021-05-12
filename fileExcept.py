#Making a code to write on a file which is opened in read mode

try:
 f=open("Demonew.txt")
 f.write("Write this thing down")
except:
 print("Something went wrong")
finally:
 f.close()
 print("Resources has been released")