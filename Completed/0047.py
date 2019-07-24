# pretty brute force, ~1min to solve, revisit?
# primes have fast gen, problem is factorization
# factorization loop is problem (43s/51s of runtime including setup)
# alternate strategies: prime seive that counts number of hits?
import prime as p
from time import clock

dur = 0

def num_unique_factors(n):
    if n <= 1: return 1
    if p.is_prime(n): return 1
    cnt = 0
    global dur
    start = clock()
    for prm in p.primes:
        if prm == 1: break
        if n < prm: continue # this line alone cuts time in half
        if n % prm == 0: cnt += 1
        while n % prm == 0: n = n//prm
    dur += clock() - start
    return cnt

hold = []
cnt = 0
for i in range(1,10**6):
    if num_unique_factors(i) == 4:
        cnt += 1
        if cnt == 4:
            print(i+1-cnt)
            print(dur)
            exit(0)
    else:
        cnt = 0
