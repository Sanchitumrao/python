# Dectionaries are mutable, unordered collections of key-value pairs.
#It can be oredered in Python 3.7 and later.
#They are defined using curly braces {} or the dict() constructor
#In dictionaries data can be accessed using keys
name=input("Enter your name:")
age=int(input("Enter your age:"))
city=input("Enter your city:")
dic1={
    'name':name,
    'age':age,
    'city':city
    }
dic2=dict(
    name=name,
    age=age,
    city=city
)
print(type(dic1))
print(type(dic2))
#Accessing values in a dictionary
print("Your Details:","User name:",dic1['name'],"age:",dic1['age'],"city:",dic1['city'])
#modifying values in a dictionary
dic1['age']=dic1['age']+1
print("Your Details:","User name:",dic1['name'],"age:",dic1['age'],"city:",dic1['city'])
#Adding new key-value pairs to a dictionary
country=input("Enter your country:")
dic1['country']=country
print("Your Details:","User name:",dic1['name'],"age:",dic1['age'],"city:",dic1['city'],"country:",dic1['country'])
#Deleting key-value pairs from a dictionary
del dic1['country']
print("Your Details:","User name:",dic1['name'],"age:",dic1['age'],"city:",dic1['city'])
