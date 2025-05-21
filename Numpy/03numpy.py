import numpy as np
#numpy array functions

#numpy array creation functions

#1. arange function()
#It is used to create an array of evenly spaced values within a given interval.
#It is similar to the built-in range() function but returns an array instead of a list.
a=np.arange(10)
print(a)
print(type(a))
print(a.dtype)#data type of array
A=np.arange(10,dtype="float")
print(A)
print(A.dtype)

b=np.arange(1,10,2)#start,end,step
print(b)

#2. linspace function()
#It is used to create an array of evenly spaced values over a specified range.
b=np.linspace(0,1,6)#start,end,number of points
print(b)
c=np.ones((3,3))#2D array of ones
print(c)
d=np.zeros((3,3))#2D array of zeros
print(d)
print(d.dtype)#data type of array
e=np.eye(3)#identity matrix
print(e)
f=np.empty((3,3))#empty array
print(f)
g=np.diag([1,2,3,4,5])#diagonal matrix
print(g)
print(np.diag(g))#extract diagonal elements
h=np.full((3,3),5)#array of 5s
print(h)

#3. random function()
#It is used to create an array of random numbers.
i=np.random.rand(3)#random numbers between 0 and 1
print(i)
j=np.random.randn(3)#random numbers from standard normal distribution
print(j)