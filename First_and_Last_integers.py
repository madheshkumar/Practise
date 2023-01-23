n=int(input())
L=list(map(int,input().split()))
x=int(input())
c=0

for i in range(x):
    if L[i]==L[n-x+i]:
        c+=1
if c == x:
    print("yes")
else:
    print("no")