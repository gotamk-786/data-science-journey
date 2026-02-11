list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 55, 1]

set1 = set(list1)
set2 = set(list2)

set1 &= set2   
result = list(set1)
print("intersection set :",result)
