#Remove the  given element from the list and print the count of elements in list.

nums=list(map(int,input().split()))
val=int(input())
count=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[count]=nums[i]
        count+=1
print(count)