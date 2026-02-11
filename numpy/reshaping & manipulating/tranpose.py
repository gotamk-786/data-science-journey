#Transpose row-->colums
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])

print(arr.T)


#Adding / Removing elements
#add
arr = np.array([1,2,3])

print(np.append(arr, 4))

#remove
arr = np.array([10,20,30,40])

print(np.delete(arr, 1))  # index 1 remove


#split array
arr = np.array([1,2,3,4,5,6])

print(np.split(arr, 3))



#Stack arrays
#Vertical stack
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))


#Horizontal stack
print(np.hstack((a,b)))
