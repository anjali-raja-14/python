# # Print the elements of even index
# l2=[]
# l1=["Anjali","Divya","Vaibhav",7,"Nancy"]
# length=len(l1)
# for i in range(length):
#     if(i%2==0):
#         l2.append(l1[i])
# print(l2)

# """
# ['Anjali', 'Vaibhav', 'Nancy']
# """


import numpy

def arrays(arr):
    arr=numpy.array(arr,arr.dtype=float)
    numpy.reverse(arr)
    
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)