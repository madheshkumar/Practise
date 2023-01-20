#Convert base a to base b

n=int(input())
a=int(input())
b=int(input())

i=0
j=0
dec=0
res=0

while n>0:
    r=n%10
    dec=dec+(r*(a**i))
    n=n//10
    i+=1

if b==10:
    print(dec)
else:
    while dec>0:
        r=dec%b
        res=res+(r*(10**j))
        dec=dec//b
        j+=1
    print(res)