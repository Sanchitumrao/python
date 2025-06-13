try:
    x=int(input("Enter number:"))
    print("Square is:",x*x)
except ValueError:
    print("Invalid input")
else:
    print("Executed without error")
finally:
    print("This block always executes")
print("------------------------Raise keyword--------------------------")
age=int(input("Enter age:"))
if age<18:
    raise ValueError("Age must be 18 or older.")
else:
    print("Access granted")
print("-----------------------------------------------------------------------")
try:
    try:
        x=int("abc")
    except ValueError:
        print("Inner try block")
    print("Outer try block")
except Exception:
    print("Outer except block")