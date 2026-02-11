"""
.revel()-->views
.flatten()-->copy

"""
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6]])
print("ravel output:",arr_2d.ravel())
print("flatten output:",arr_2d.flatten())


"""
indexing
slicing
fancy indexing
boolean masking
array reshape
ravel,flatten

"""

#Flattening (2D → 1D)

arr = np.array([[1,2,3],[4,5,6]])

print(arr.flatten())
print(arr.ravel())
