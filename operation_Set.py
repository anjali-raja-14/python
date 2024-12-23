set1={'Ram','shyam','jenny'}
set2={'jiya','aakash','jenny'}
set3={'Anjali','Ravi','yash'}

# union
print(set1.union(set2))
print(set1|set2)
print(set1.union(set2,set3))
print(set1.union((1,2,3)))
tuple1=(1,2,3)
# print(set1|tuple)     >>>operand not supported

(set1.update('a','b'))
print(set1)

# intersection

print(set1.intersection(set2))
print(set1&set2)
set1.intersection_update(set2)
print(set1)
print("disjoint")
print(set1.isdisjoint(set2))