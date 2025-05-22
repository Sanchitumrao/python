#tuple methods 
# 1. count()#returns the number of occurrences of a value in a tuple
# 2. index()#returns the index of the first occurrence of a value in a tuple
# 3. len()#returns the number of elements in a tuple
# 4. min()#returns the smallest element in a tuple
# 5. max()#returns the largest element in a tuple
# 6. sorted()#returns a sorted list of the elements in a tuple
# 7. all()#returns True if all elements in a tuple are true (or if the tuple is empty)
# 8. any()#returns True if any element in a tuple is true (or if the tuple is empty)
# 9. sum()#returns the sum of all elements in a tuple
# 10. tuple()#converts iterable to a tuple

t=(1,2,3,2,3,3,4,5,6,7,8,9,10)
print("count of 3 in tuple is: ",t.count(3))
print("index of 3 in tuple is: ",t.index(3))
print("length of tuple is: ",len(t))
print("minimum value in tuple is: ",min(t))
print("maximum value in tuple is: ",max(t))
print("sorted tuple is: ",sorted(t))#this returns a sorted list
print(type(sorted(t)))
tup=(1,2,3,4,5)
print("sum of tuple is: ",sum(tup))

t=(True,False,True)
print("all elements in tuple are true: ",all(t))
print("any element in tuple is true: ",any(t))

# converting list to tuple
list=[1,2,3,4,5]
tup2=tuple(list)
print("list to tuple: ",tup2," type: ",type(tup2))
# converting string to tuple
str="hello"
tup3=tuple(str)
print("string to tuple: ",tup3," type: ",type(tup3))