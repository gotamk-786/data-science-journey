import numpy as np
"""
start-->staring index 1
stop-->end index kahan stop karna and yhe exclude hoga if pass 3then 3-1=2 access karen ga
step-->(default)1
aarr[start:end], start to end-1
negative step, -1 reverse

"""
arr=np.array([10,20,30,40,50,60])
print(arr[1:5]) # end-1=5-1=4 index lastnindex 1 to 4
print(arr[:4])# index 0 to 3
print(arr[::2]) # every second element
print(arr[::-1]) # without loop reverse the array in numpy
