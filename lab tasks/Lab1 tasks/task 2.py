size=int(input("enter the size of list:"))
nums=[]
even=0
odd=0
for i in range(size):
    num=int(input("enter number:"))
    nums.append(num)
    if num%2==0:
        even+=1
    else :
        odd+=1
     
print(nums)
print("total even:",even)
print("total odd:",odd)
