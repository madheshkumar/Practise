n, x = map(int, input().split())
temp = n
t1, t2 = 0, 0
rev = 0
while temp > 0:
    a = temp % 10
    rev = rev * 10 + a
    temp //= 10
while n > 0:
    a = n % 10
    b = rev % 10
    if x == 1:
        t1, t2 = a, b
    x -= 1
    n //= 10
    rev //= 10
print(t1 * t2)
