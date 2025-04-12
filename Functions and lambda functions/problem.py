# wa python program to find the larger of two nos
def larger(a,b):
    if(a>b):
      return a
    else:
       return b
a=larger(89,5)
print(a)

# using lambda fun
large=(lambda a,b :a if a>b else b)
print(large(6,7))
