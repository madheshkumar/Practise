n,x,y=map(int,input().split())
L=list(map(int,input().split()))
res=0

for i in range(n):
    if L[i]>=x and L[i]<=y:
        res+=L[i]
print(res)