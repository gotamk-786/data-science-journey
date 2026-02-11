import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr[arr>25])



result = arr[arr > 25]
print(result)

#evenand odd filtering
arr = np.array([1, 2, 3, 4, 5, 6])

even = arr[arr % 2 == 0]
print("even:",even)


# logical operations
arr = np.array([5, 10, 15, 20, 25])

res = arr[(arr > 10) & (arr < 25)]
print(res)
# boolean array
arr = np.array([10, 25, 30, 5, 40])

mask = arr >= 25
print(mask)
print(arr[mask])
