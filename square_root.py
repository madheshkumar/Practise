x=int(input())
if x <=1:
    print(x)

i=1
temp=i*i
while(x>=temp):
    i+=1
    temp=i*i
print(i-1)