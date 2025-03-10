import numpy as np
x=np.array([1,2,3,4,5])
print("Min: ",np.min(x))
print("Max: ",np.max(x))
print("sqrt: ",np.sqrt(x))
print("Position of minimum value: ",np.argmin(x))
print("Position of maximum value: ",np.argmax(x))
print(np.min(x,axis=0))
print(np.cos(x))
print(np.sin(x))
print(np.cumsum(x))#cumulative sun
""""
Min:  1
Max:  5
sqrt:  [1.         1.41421356 1.73205081 2.         2.23606798]
Position of minimum value:  0
Position of maximum value:  4
1
[ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
[ 1  3  6 10 15]
"""