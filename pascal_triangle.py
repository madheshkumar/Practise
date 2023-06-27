n=int(input())
for i in range(1,n+2):
    if i!=2:
        c=1
        for j in range(i):
            if j==0 or j+1==i:
                print(1,end=" ")
            else:
                c=(c*(i-j))//j
                print(c,end=" ")
        print()
