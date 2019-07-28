import prime as p
from itertools import combinations as combos
from time import clock

family = 8
m = 0

for i in range(2,6+1):
    mark = m
    p.build_primes(10**i)
    m = len(p.primes)
    #if i < 6: continue
    for prime in p.primes[mark:]:
        s = str(prime)[::-1]
        for c in range(0,10-family+1):
            loc = []
            l = -1
            while True:
                l = s.find(str(c),l+1)
                if l == -1: break
                loc.append(l)
            for filt in [c for r in range(len(loc)) for c in combos(loc,r+1)]:
                cnt, mss = 1, 0
                nsrt = sum( 10**f for f in filt )
                num = prime
                for r in range(c+1,10):
                    num += nsrt
                    if p.is_prime_fast(num):
                        cnt += 1
                        if cnt == family:
                            print(prime,filt)
                            exit(0)
                    else:
                        mss += 1
                        if mss > 10-family: break
