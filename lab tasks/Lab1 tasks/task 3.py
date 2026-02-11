size=int(input("enter the size of list:"))
nums=[]
for i in range(size):
    num=int(input("enter number:"))
    nums.append(num)

print(nums)

def greater(list,n):
    count=0
    for i in list:
        if i>n:
            count+=1
    return count

digit = int(input("Enter the number to count greater than: "))
result=greater(nums,digit)
print("numbers greater than :",result)
    
