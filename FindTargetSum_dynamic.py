def canSum(target, elements, mem={}):
    if target in mem:
        return mem[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for e in elements:
        rem = target - e
        if canSum(rem, elements, mem) == True:
            mem[target] = True
            return mem[target]
    mem[target] = False
    return mem[target]

print(canSum(300, [7, 14]))
