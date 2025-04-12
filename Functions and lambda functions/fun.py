#functions in python
# functions are blocks of code that only run when they are called
# they can take arguments and return data as a result
# functions are defined using the def keyword

# fun definitation
def greet(name):
    print("good day",name)

# function call
greet("sanchit")


# function with returning value
def add(a,b):
    c=a+b
    return c
    
b=add(3,4)
print(b)

print(type(b))
print(type(add))

# function with returning no value
def add(a,b):
    c=a+b
    return None

