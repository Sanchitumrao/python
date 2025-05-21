#Tuples in python
# Tuples are immutable,unchangable,iterable and can be hetrogenious 

#creating a tuple
t=(2,"Ram",3.06,False,)
print("tuple=",t)
print(type (t))

#tuples are ordered
a=t[0]
b=t[1]
print("t[0]=",a,",type of t[0]",type(a))#accessing the first element of the tuple
print("t[1]=",a,",type of t[1]",type(b))#accessing the second element of the tuple

#tuples are iterable
for i in t:
    print(i)


#tuples are immutable
# t[0]=5  #this will give an error

#creating a tuple with one element
t1=(2,)#tuple with one element needs a comma
t2=(2)#this is not a tuple 
print("t1=",t1,",type of t1",type(t1))
print("t2=",t2,",type of t2",type(t2))

#empty tuple
t3=()
print("t3=",t3,",type of t3",type(t3))

# concatination of tuples
t4=t+t1
print("t4=",t4,",type of t4",type(t4))

# Membership test
print(2 in t)#True

#nesting of tuples
tup=(1,2,3,(4,5,6),7)
print("tup=",tup)

#nesting of lists in tuples
tup1=(1,2,3,[4,5,6],7)
print("tup1=",tup1)

tup1[3][0]=10#changing the value of 4 to 10
print("changed tup1=",tup1)