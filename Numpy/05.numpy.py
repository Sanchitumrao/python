import numpy as np
#indexing and slicing

a=np.arange(10)
print(a)
print(a[0])

b=np.diag([1,2,3,4,5])
print(b)
print(b[4,4])#row,column 5

b[4,4]=10#change value of 5th element to 10
print(b)

#slicing
print(a[0:5])#start:end
print(a[0:5:2])#start:end:step

# we can also combine assignment and slicing
a[5:]=10
print(a)