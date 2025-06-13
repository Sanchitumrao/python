f=open("01.txt")
lines=f.readlines()
for line in lines:
    print(line,end="")
f.close()
print("")
print("-----------------------------------")
#with keyword in python
with open("05.txt","w")as f:
    f.write("welcome to the python\nThis is file handling in python\n")
print("Is file closed:",f.closed)
print("---------------------read()-------------------")
f=open("05.txt","r")
print(f.tell())
print(f.read(5))
print(f.tell())
print(f.read(10))
print(f.tell())