#Open the file in append mode

f=open("Demonew.txt","a")
f.write("Wow that's sounds great(additional content)")
f.close()

#Open agian and read the file
g=open("Demonew.txt","r")
print(g.read())
g.close()