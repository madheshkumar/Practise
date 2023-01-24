n=int(input())
for i in range(n):
    for j in range(1,n+1):
        if i==0 or i==n-1:
            print(j,end=" ")
        elif j==n-i:
            print(n-i,end=" ")
        elif j<n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#input
#  8

#output
#   1 2 3 4 5 6 7 8 
#   * * * * * * 7   
#   * * * * * 6     
#   * * * * 5       
#   * * * 4
#   * * 3
#   * 2
#   1 2 3 4 5 6 7 8 
