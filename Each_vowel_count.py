n=input()
V=[0,0,0,0,0]

for i in range(len(n)):
    if n[i]=='a':
        V[0]+=1
    if n[i]=='e':
        V[1]+=1
    if n[i]=='i':
        V[2]+=1
    if n[i]=='0':
        V[3]+=1
    if n[i]=='u':
        V[4]+=1
    
print("a",V[0])
print("e",V[1])
print("i",V[2])
print("o",V[3])
print("u",V[4])