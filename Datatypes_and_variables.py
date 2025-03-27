# Datatypes and variables 
x=10 # integer
y=3.14 # float
name="Sanchit" # string
is_valid=True # boolean

print(x,y,name,is_valid) # print variables
print(type(x),type(y),type(name),type(is_valid)) # print datatypes of variables
# type(object) is a built-in function in python.It is used to check the data type of variable or object


# typecasting:convertingone datatype to another
# int to float
a=10
b=float(a)
print(b) # 10.0
# float to int

c=3.14
d=int(c)
print(d) # 3
# string to int
e="45"
f=int(e)
print(f) # 45

# int to string
g=10
h=str(g)
print(h) # "10"

# float to string
i=3.14
j=str(i)
print(j) # "3.14"