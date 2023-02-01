ch1,ch2=map(str,input().split())
val1=ord(ch1)
val2=ord(ch2)
vow="AEIOUaeiou"
count=0

for i in range(val1,val2+1):
    if chr(i) not in vow:
        count+=1

print(count)