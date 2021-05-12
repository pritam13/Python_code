#create new file
f=open("NewFile.txt","x")
f.write("Created this new file. It is really cool.")
f.close()
#Read the newly created file

g=open("NewFile.txt","r")
print(g.read())
g.close()