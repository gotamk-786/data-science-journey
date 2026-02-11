size = int(input("enter the size of list: "))
nums = []

for i in range(size):
    num = int(input("enter number: "))
    nums.append(num)

print("original list:", nums)

new_list = []
for i in nums:
    if i >= 0:
        new_list.append(i)
print("list after removing negative values:", new_list)
