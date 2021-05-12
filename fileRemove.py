#Check file exist or not
import os
if os.path.exists("NewFile.txt"):
 os.remove("NewFile.txt")
else:
 print("File does not exists")