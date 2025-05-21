import numpy as np
# numpy data types

# 1. int
a=np.array([1, 2, 3])
print(a.dtype) # int64
# 2. float
b=np.array([1.0, 2.0, 3.0])
print(b.dtype) # float64
# 3. complex
c=np.array([1+2j, 2+4j])
print (c) 
print(c.dtype) # complex128
# 4. bool
d=np.array([True, False])
print(d)
print(d.dtype) # bool
# 5. string
e=np.array([ 'Ram', 'Robert'], dtype='S')# string of length 6
print(e)
print(e.dtype) 

# 6. unicode
f=np.array([ 'Ram', 'Robert'])# unicode string of length 6
print(f)
print(f.dtype)

# 7. object
g=np.array([1, 'Ram', 2.0])# object array
print(g)
print(g.dtype) 

