#set Operations
# # Union
s1={1,2,3,4,5}
s2={2,3,4,5,6}
s3=s1.union(s2)
print("S1=",s1,)
print("S2=",s2)
print("Union of s1 and s2:",s3)
# # Intersection
s4=s1.intersection(s2)
print("Intersection of s1 and s2:",s4)
# # Difference
s5=s1.difference(s2)
print("Difference of s1 and s2:",s5)
# # Symmetric Difference
s6=s1.symmetric_difference(s2)
print("Symmetric Difference of s1 and s2:",s6)
# # Subset
s7={1,2}
s8={1,2,3,4,5}
print("s7=",s7)
print("s8=",s8)
print("Is s7 subset of s8:",s7.issubset(s8))
# # Superset
print("Is s8 superset of s7:",s8.issuperset(s7))
# # Disjoint Sets
s9={1,2,3}
s10={4,5,6}
print("s9=",s9)
print("s10=",s10)
print("Are s9 and s10 disjoint sets:",s9.isdisjoint(s10))
# # Copying a set
s11=s1.copy()
print("Copy of s1:",s11)