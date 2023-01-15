# Input: digits = [1,2,3]
# Incrementing by one gives 123 + 1 = 124.
# Output: [1,2,4]

# using recursion

l=list(map(int,input().split()))
n=len(l)-1

def add(n):
    if n==-1:
        l.insert(0, 1)
        return
    
    if l[n]>=0 and l[n]<9:
        l[n]=l[n]+1
    else:
        l[n] = 0
        add(n-1)
        
add(n)
print("Result:",l)