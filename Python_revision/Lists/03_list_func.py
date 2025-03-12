x=[True,0,False]
print(min(x))
print(max(x))
x.extend([1,2,3,4]) #add at the end of the list
print(x)
x[0:3]=[66,7,8,9,1]
print(x)
print(x.pop())
x.reverse()
print(x)
print(x.count(1))
"""
0
True
[True, 0, False, 1, 2, 3, 4]
[66, 7, 8, 9, 1, 2, 3, 4]
4
[3, 2, 1, 9, 8, 7, 66]
"""