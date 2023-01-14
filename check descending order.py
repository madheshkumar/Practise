n=int(input())
L=list(map(int,input().split()))
flag=1
t=L[0]
for i in range(n):
    if L[i]>t:
        flag=0
    t=L[i]
if flag:
    print("yes")
else:
    print("no")
