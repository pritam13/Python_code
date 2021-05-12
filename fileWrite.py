#Open a file and Overwrite its content using "w"
f=open("Demonew.txt","w")
f.write("This is a brand new content.")
f.close()

#Read the newly written file

g=open("Demonew.txt","r")
print(g.read())
g.close()