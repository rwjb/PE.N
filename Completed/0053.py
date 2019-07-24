fact = {0:1}
for f in range(1,100+1):
    fact[f] = fact[f-1] * f
millions = 0
for n in range(23,100+1):
    mill = n + 1
    for r in range((n+1)//2):
        num = fact[n] / ( fact[r] * fact[n-r] )
        if num > 10**6:
            millions += mill
            break
        else:
            mill -= 2
print(millions)
