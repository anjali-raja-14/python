import numpy as np
# x=np.array([1,2,3,4])
# print(x.dtype)

"""
int64
"""

# Change datatype of an array

# x=np.array([1,2,3,4],dtype=np.int8)
# print(x.dtype)
"""
int8
"""


# change the full array using datatypes
x=np.array([1,2,3],dtype="f")
print(x)

"""
[1. 2. 3.]
"""



# change the datatypes using function

# x=np.array([1,2,3])
# new=np.float32(x)
# print("Datatype:",x.dtype)
# print("Datatype:",new.dtype)
# print(x)
# print(new)

""""
Datatype: int64
Datatype: float32
[1 2 3]
[1. 2. 3.]

"""
# change the datatypes using function

new=np.dtype(float)
x=np.array([1,2,3],new)
print(x.dtype)

""""
[1. 2. 3.]
float64
"""

