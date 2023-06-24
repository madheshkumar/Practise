def grid(i,j,mem={}):
    if (i,j) in mem:
        return mem[(i,j)]
    if i<1 or j<1:
        return 0
    if i==1 and j==1:
        return 1
    else:
        print(i,j,mem)
        mem[(i,j)]=grid(i-1,j,mem)+grid(i,j-1,mem)
        return mem[(i,j)]

print(grid(3,3))
