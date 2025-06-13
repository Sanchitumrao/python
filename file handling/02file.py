f=open("03.txt","w")
lst=["Satyam\n","Sanchit\n","Saurabh\n","Pranjul\n",]
f.write("welcome\n")
f.writelines(lst)
print("List of lines written successfully")
f.close()