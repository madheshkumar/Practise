def fibo(n,mem={}):
    if n in mem:
        return mem[n]
    if n <=1:
        return 1
    else:
        mem[n]= fibo(n-1,mem)+fibo(n-2,mem)
        return mem[n]

print(fibo(6))
print(fibo(8))
print(fibo(10))
print(fibo(100))
