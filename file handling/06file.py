f1=open("1.jpg","rb")
f2=open("2.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("New image is available with the name 2.jpg")
print("-------------working with csv file-------------")
import csv
with open("emp.csv","w",newline="")as f:
    w=csv.writer(f)
    w.writerow(["EmpID","EmpName","EmpSal"])
    n=int(input("Enter no of employees:"))
    for i in range(n):
        Eid=input("Enter emp Id:")
        EName=input("Enter emp Name:")
        ESal=input("Enter emp Salary:")
        w.writerow([Eid,EName,ESal])
    print("Data Written to csv file successfully.")
print("------------------------------------")
import csv
with open("emp.csv",newline="")as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)