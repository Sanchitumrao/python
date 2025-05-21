import numpy as np
a=np.array([1,2,3])

print(a)
# using python lists
L=range(1000)
print ([i**2 for i in L]) 
# execution time: 0.1s

#??Why we use numpy??

# using numpy arrays 
# 200 times faster

a=np.arange(1000)
print (a**2)
# execution time: 0.01s