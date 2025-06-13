#exception handling in python

print("One")
print("Two")
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception passed")
print("Four")
print("Five")


print("----------------------------------------------")

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
try:
    print("Division is:",a/b)
except ZeroDivisionError:
    print("Division is not possible!!!!!!!!!")

print("---------------------------------------------")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
try:
    c=a/(a-b)
    print("value of c is:",c)
except ZeroDivisionError as z:
    print("Exception passed!!!",z)
d=a/(a+b)
print("Value of d is:",d)
print("---------------------------------------------")
try:
    x=int("hello")
    y=10/0
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("ZeroDivisionError occured")

print("---------------------------------------------")
try:
    x=("hello")
    print(x)
    y=10/0
    print(y)
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("ZeroDivisionError occured")
print("-----------------------------------------------")
try:
    a=10/0
except Exception as e:
    print("Error:",e)