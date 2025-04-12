#lambda function 
# lambda function is a small anonymous function means it does not have a name
# it can take any number of arguments but can have only one expression means it can return only one value
# the expression is evaluated and returned 
# it can be used to create small functions that are not reused elsewhere
# it is often used as an argument to higher-order functions (functions that take other functions as arguments)


a=(lambda a,b:a+b)(3,4)
print(a)

#add using user defined function
def func(a,b):
    return a+b
add=func(3,4)
print(add)
 
ad=(lambda c,d:c+d)
print(ad(3,4))