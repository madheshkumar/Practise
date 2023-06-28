n=int(input())
def isHappy(n,Arr=[]):

    if n==1:
        return True
    if n not in Arr:
        Arr.append(n)
        s=0
        while(n>0):
            d=n%10
            s+=d**2
            n//=10
        return isHappy(s,Arr)
    return False

print(isHappy(n))