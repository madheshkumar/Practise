r,c=map(int, input().split())
L=[]
for i in range(r):
    x=list(map(int, input().split()))
    L.append(x)
for i in range(r):
    if(i%2==1):
        L[i].reverse()
for j in range(c):
    if(j%2==0):
        st=0
        en=r-1
        while(st<en):
            temp=L[st][j]
            L[st][j]=L[en][j]
            L[en][j]=temp
            st+=1
            en-=1
for i in range(r):
    for j in range(c):
        print(L[i][j],end=" ")
    print()