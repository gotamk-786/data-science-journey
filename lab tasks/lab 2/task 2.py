first = [11.25, 18.0, 20.0, 10.75, 9.50]
second = [10.75, 9.50]

full = first + second
print("Merged list:", full)

full_sorted = sorted(full, reverse=True)
print("Sorted list (descending):", full_sorted)

full_sorted.append(24.5)
full_sorted.append(15.45)
print("After appending:", full_sorted)
full_sorted.reverse()
print("After reversing:", full_sorted)

import math
radius = 5   
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Circumference of circle:", circumference)
print("Area of circle:", area)
