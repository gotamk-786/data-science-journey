"""
reshpae(rows,columns) specify new shape
if dimensions match then reshaped possible
"""

import numpy as np
arr = np.array([1,2,3,4,5,6])
print("before reshpaed:",arr)
new_arr = arr.reshape(2,3)
print("after reshaped:",new_arr)

#1D → 2D → 3D reshape

arr = np.arange(12)

print(arr.reshape(3,4))     # 2D
print(arr.reshape(2,2,3))   # 3D

#-1 ka use (NumPy khud calculate kare)
arr = np.arange(8)

print(arr.reshape(2,-1))
