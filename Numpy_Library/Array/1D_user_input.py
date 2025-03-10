# convert user input list into array

import numpy as np
l=[]
inp=int(input("Enter, how many elements do you want:  "))
for i in range(1,inp+1):
    n=int(input("Enter the number: "))
    l.append(n)
    l_array=np.array(l)
print(l_array)
# print the dimension of array
print(f"{l_array.ndim}D array")


"""
Enter, how many elements do you want:  3
Enter the number: 1
Enter the number: 2
Enter the number: 3
[1 2 3]
1D array
"""





