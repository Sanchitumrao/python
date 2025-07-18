import numpy as np
# Numpy is a powerful library for numerical computing in Python

# 1D array

a=np.array([0,1,2,3]) #vector
print (a)
print (a.shape)
print (a.ndim)
print (a.dtype)

# 2D array
b=np.array([[0,1,2],[3,4,5]])#matrix
print (b)
print (b.shape)
print (b.ndim)

# 3D array
c=np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])#tensor
print (c)
print (c.shape)
print (c.ndim)
