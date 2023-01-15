# add or subtract elemnt from x

n=int(input())
L=list(map(int,input().split()))
x=int(input())

for i in range(n):
    if L[i]<x:
        print(L[i]+x,end=" ")
    else:
        print(L[i]-x,end=" ")