#sets are unordered, unindexed, and mutable collections of unique elements
# they are defined using curly braces {} or the set() constructor
s={1, 2, 3, 4, 5}

s2=set([1, 2, 3, 4, 5])
print(type(s)) # <class 'set'>
print(type(s2)) # <class 'set'>
print(s is s2) # False
print(s == s2) # True
print(id(s))
print(id(s2)) #Ids of s and s2 are different 

# Empty set
s3=set()
s4={}# this is an empty dictionary we can not use this to create an empty set
print(type(s3)) # <class 'set'>
print(type(s4)) # <class 'dict'>
#sets are unordered
s5={1,5,2,3,4}
print(s5) 
#unique elements
s6={1, 2, 3, 4, 5,5,5,5,6}#It will only keep unique elements
print(s6,"Type",type(s6)) # {1, 2, 3, 4, 5}
#Sets are mutable
s7={1, 2, 3, 4, 5}
s7.add(6) # add an element
print(s7) 
#sets are unindexed
s8={1, 2, 3, 4, 5}
# print(s8[0]) # TypeError: 'set' object is not subscriptable