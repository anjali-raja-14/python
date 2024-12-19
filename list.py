# Indexing possible
# Store values of diffrent data types
# Mutable
# Slicing possible
# Methods>>
# list.append()
# list.sort()
list=[0,1,14,3,4,0,9]
name=["cat","anjali","banana"]
print(list[0])
print(list)
print(name)
print("Methods\n")

list.append(10)
print("Append: ",list)

list.sort()
print("sort: ",list)

list.sort(reverse=True)
print("Sort decending: ",list) 

list.reverse()
print("Reverse: ",list)

list.insert(0,9)
print(list)

list.remove(1)
print(list)
list.pop(2)
print(list)