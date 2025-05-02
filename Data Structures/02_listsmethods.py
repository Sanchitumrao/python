# List methods in python
lst=["apple","orange",5,3.06,False,"aakash","rohan"]
print(lst)

lst.append("sanchit")
print(lst)

l1=[2,45,78,40,56,23,12,34,1,90]
print("Original list:",l1)
l1.sort()#sorting the list in ascending order
print("Sorted list:",l1)

l1.reverse()#reversing the list
print("Reversed list:",l1)

l1.insert(3,4565)#inserting 4565 at index 3
print("Inserted list:",l1)

value=l1.pop(2)#removing the value at index 2 and returning it
print(value)

print("Popped list:",l1)

l1.remove(45)#removing the first occurrence of 45 from the list
print("Removed list:",l1)


l1.clear()#clearing the list
print("Cleared list:",l1)

l1.extend([1,2,3,4,1,5])#adding multiple values to the list
print("Extended list:",l1)

l1.copy()#copying the list
print("Copied list:",l1)


l1.count(1)#counting the number of occurrences of 1 in the list
print("Count of 1 in list:",l1.count(1))