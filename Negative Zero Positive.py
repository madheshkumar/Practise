n=int(input())
L=list(map(int,input().split()))
for j in range(3):
    for i in range(len(L)-1,-1,-1):
        if L[i] < 0 and j == 0:
            print(L[i],end=" ")
        if L[i] == 0 and j == 1:
            print(L[i],end=" ")
        if L[i] > 0 and j == 2:
            print(L[i],end=" ")