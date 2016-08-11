def div_all(n):
    factors = []
    for i in range(2,n+1):
        num = i
        for f in factors:
            if num % f == 0:
                num /= f
        while num % 2 == 0:
            num /= 2
            factors += [2]
        for j in range(3,int(i**.5)+2,2):
            while num % j == 0:
                num /= j
                factors += [j]
        if num > 1:
            factors += [i]
    ret = 1
    for f in factors: ret *= f
    return ret
print(div_all(10))
print(div_all(20))
