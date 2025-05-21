# strings in python


# strings are a sequence of characters
# strings are immutable
# strings are ordered
# strings are indexed
# strings are iterable
# strings are hashable i.e. they can be used as keys in dictionaries
# strings are objects


a="Sanchit Umrao"

# a='Sanchit Umrao' # single line string
# a='''Sanchit Umrao''' multi line strings
print(len (a))
firstname=a[0:8]
lastname=a[7:]
print("First name:",firstname)
print("Last name:",lastname)
char0=a[0]
char1=a[1]
char2=a[2]
char3=a[3]
char4=a[4]
char5=a[5]
char6=a[6]
char7=a[7]
print(char0,char1,char2,char3,char4,char5,char6,char7)

# slicing

print(a[-5:-1])#slicing with negative index
print(a[8:13])# slicing with positive index
print(a[:7])# slicing with default value
print(a[0:7])
print(a[7:])
print(a[0:])
print(a[0:-6]) # slicing with step value


# slicing with skip value
word="Welcome"
print(word[1:6:2])#ecm index 1 to 6 with skip value of 2 