# print the count of sum of first and last element

n=int(input())
L=list(map(int,input().split()))
s=L[0]+L[n-1]
count=0

for i in range(1,n-1):
    if L[i]==s:
        count+=1
print(count)