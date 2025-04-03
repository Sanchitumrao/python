# operators in python
a=1
b=3
# arithmetic operators
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(a//b) # floor division
print(a**b) # exponentiation
print(a%b) # modulus

# assignment operators
print(a) # a=1

a+=3 # a=a+3
print(a) # a=4
a-=3 # a=a-3
print(a) # a=1
a*=3 # a=a*3
print(a) # a=3
a/=3 # a=a/3
print(a) # a=1.0
a//=3 # a=a//3
print(a) # a=0.0
a**=3 # a=a**3
print(a) # a=0.0
a%=3 # a=a%3
print(a) # a=0.0

a=1 # reset a to 1
b=3 # reset b to 3

# comparison operators

print(1==1)# equal to
print(5<=6)# less than or equal to
print(5<=4)
print(5==4)
print(5!=4)# not equal to
print(5>4)# greater than
print(5<4)# less than
print(5>=4)# greater than or equal to


# logical operators and ,or, not

e= True or False
print(e)
# truth table for or 
print("true or false is",True or False)
print("true or true is",True or True)
print("false or true is",False or True)
print("false or false is",False or False)
# truth table for and
print("true and false is",True and False)
print("true and true is",True and True)
print("false and true is",False and True)
print("false and false is",False and False)
print(not(True))
print(not(False))

#bitwise operators
# & , | , ^ , ~ , << , >>
print(5&3) # bitwise and
print(5|3) # bitwise or
print(5^3) # bitwise xor
print(~5) # bitwise not
print(5<<3) # left shift
print(5>>3) # right shift

# identity operators
# is , is not
print(5 is 3) # is
print(5 is not 3) # is not
print(5 is 5) # is


# membership operators
# in , not in
print(5 in [1,2,3,4,5]) # in
print(5 not in [1,2,3,4,5]) # not in