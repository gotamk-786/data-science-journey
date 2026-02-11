import numpy as np
list2d = [[180, 78.4],
          [215, 102.7],
          [210, 98.5],
          [188, 75.2]]

nplist2d = np.array(list2d)

print("Type of list2d:", type(nplist2d))
print("Shape of list2d:", nplist2d.shape)

print("Second column:", nplist2d[:, 1])

print("3rd row, 0th column:", nplist2d[2, 0])

np_height = nplist2d[:, 0]
print("np_height:", np_height)

print("Mean of np_height:", np.mean(np_height))
print("Median of np_height:", np.median(np_height))
print("Standard deviation of np_height:", np.std(np_height))
