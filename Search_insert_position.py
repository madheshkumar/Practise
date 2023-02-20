nums=list(map(int,input().split()))
target=int(input())

l = 0
r = len(nums) - 1
while r >= l:
    mid = (l + r) // 2
    if target > nums[mid]:
        l = mid + 1
    elif target <= nums[mid]:
        r = mid - 1
print(l)