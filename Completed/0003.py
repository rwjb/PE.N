#num = 13195
num = 600851475143
factors = []
while num % 2 == 0:
    factors += [2]
    num /= 2
div = 3
while num != 1:
    while num % div == 0:
        factors += [div]
        num /= div
    div += 2
print(max(factors))
