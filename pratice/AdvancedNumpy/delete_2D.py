# delete 2D array
import numpy as np
arr_2D=np.array([[1,2,3],[4,5,6]])
print(arr_2D)
new_arr_2d=np.delete(arr_2D,0,axis=0) #0 index wali row pori delte here
print(new_arr_2d)
