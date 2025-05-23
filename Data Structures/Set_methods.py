# Add an element to a set
s={1,2,3}
print("Set=",s)
s.add(4)
print("4 Added on set:",s)
#remove an element from a set
s.remove(2)
print("2 Removed from set:",s)
#discard an element from a set
s.discard(3)
print("3 Discarded from set:",s)
#pop an element from a set
s.pop()
print("Poped set:",s)
#clear a set
s.clear()
print("Cleared set:",s)
#update a set
s.update({1,2,3,4,5})
print("Updated set:",s)

