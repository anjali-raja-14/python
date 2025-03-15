# Set can't store list &  dict bcs..it it mutable (can be changed)
# Duplicate are allowed but can be print once only
# mutable
# set (mutable)
# set's elements (immutable)

collection={1,2,3,"Anjali","Raja","Raja"}
print(collection)
# {1, 2, 3, 'Raja', 'Anjali'}

# To create an empty set
collection_1=set()
collection_1.add(2)
collection_1.add(2)
collection_1.add(4)
collection_1.add(0)

print(len(collection_1))#3

print(collection_1)#{0, 2, 4}
collection_1.remove(2)
print(collection_1)
print(len(collection_1))#2
print("pop:",collection_1.pop())
collection_1.clear()
print(collection_1)
 

