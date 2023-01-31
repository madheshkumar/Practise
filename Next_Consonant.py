#find the next Consonant

ch=input()
val=ord(ch)
vow="AEIOUaeiou"
for i in range(val+1,123):
    if chr(i) not in vow:
        print(chr(i))
        break
