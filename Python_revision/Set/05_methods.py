set1={1,2,3,4,5,6}
set2={7,8,9,10,11,12}
print(set1.isdisjoint(set2)) # True

set3={1,2,3,4,5}
set4={1,0,4,8,9,3,2,5}
print(set3.issubset(set4)) # True
print(set3.issuperset(set4)) #False 
# super- Every element if set4 present in set3
