tuple1=(1,2,3,4,5,5,5)
tuple2=(5,4,3,21)
tuple3=tuple1+tuple2
print(tuple3)
length=len(tuple3)
count=tuple1.count(5)
print(f"count of 5: {count}")
print(f"Length: {length}")#length=9

tuple3=tuple1,tuple2
print(tuple3)
length=len(tuple3)
print(f"Length: {length}")#length=2

tuple4=(1,"Anjali","jenny","Vaibhav")
print(tuple4)
print(tuple4[1:3])

tuple5=(1,)
print(tuple5)

# Tuple is just like a list but have () brackets.
# we can do may operation in tuple 
# we can not change  and  delete the member
# It is immutable
# Nesting is also possible
# Count function is also possible 
# Indexing is also possible