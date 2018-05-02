from time import clock
now = clock()
from math import sqrt
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0 and 2 < n:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
def trunc_prime(n):
    if n<10: False
    nn = str(n)
    candidates = [n]
    for i in range(1,len(nn)):
        candidates.append(int(nn[:i]))
        candidates.append(int(nn[i:]))
    return all(is_prime(c) for c in candidates)
i = 11
tprimes = []
while len(tprimes) < 11:
    if not any(int(digit)%2==0 for digit in str(i)[1:]) \
       and not any(int(digit)%5==0 for digit in str(i)[1:]) \
       and trunc_prime(i):
        tprimes.append(i)
        print(len(tprimes),i)
    i += 2
print(sum(tprimes))
# 748317
print("Duration:",clock()-now)
