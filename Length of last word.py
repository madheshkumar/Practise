#Count the length of last word of string

s=input()
count=0
flag=0
for i in range(len(s)-1,-1,-1):
    if s[i]==" " and flag==0:
        continue
    elif s[i]!=" " or flag==0:
        count+=1
        flag=1
    else:
        break
print(count)
                
        
   