n=int(input())        #no. of x,y values
nums=list(map(int,input().split()))
t=1
for i in range(n+1,len(nums)):
    s=i-1
    while(s!=t):
        temp=nums[s]
        nums[s]=nums[s-1]
        nums[s-1]=temp
        s-=1
    t+=2
print(nums)

#input  n=3 [x1,x2,x3,y1,y2,y3]
#output [x1,y1,x2,y2,x3,y3]