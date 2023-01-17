n,x=map(int,input().split())
f=0
for i in range(n):
    a=input().strip()
    if len(a)!=x:
        print(a)
        f=1
if f==0:
    print(-1)  