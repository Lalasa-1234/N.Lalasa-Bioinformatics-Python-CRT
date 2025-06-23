my_set={1,2,3,4,5,6,7,8,9}
print(type(my_set))
print(1 in my_set)
my_set.add(11)
my_set.update(['apple','grape'])
my_set.remove(1)
my_set.discard(2)
my_set.clear()
print(my_set)

#operations in set
set1={1,2,3}
set2={3,4,5}
print(set1 | set2)#union operator
print(set1 & set2)#intersection-common elements
print(set1 - set2)#DIFFERENCE-elements only in first set 
print(set1 ^ set2)#SYMMETRIC DIFFERENCE-return non common elements in bot sets

#builtin functions and methods
#intersection()
#union()
#difference()
#issubset()
seta={1,2,3,4}
setb={1,2,3,4,5,6,7,8,9}
print(seta.issubset(setb))
print(setb.issubset(seta))
#issuperset()
print(seta.issuperset(setb))
print(setb.issuperset(seta))

