n=int(input())
L=list(map(int,input().split()))
for i in range(0,n,2):
    if L[i]>L[i+1]:
        print(L[i+1],end=" ")
        print(L[i],end=" ")
    else:
        print(L[i],end=" ")
        print(L[i+1],end=" ")

#input:
# 4
# 10 5 2 4
#output
# 5 10 2 4