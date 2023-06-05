n=int(input())
L=[]
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n//=10
while(rev>10):
    d1=rev%10
    rev//=10
    d2=rev%10
    rev//=10
    L.append(d1*d2)
if rev!=0:
    L.append(rev)
for i in range(len(L)):
    print(L[i],end=" ")


