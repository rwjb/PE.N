from math import sqrt
primes = [2,3]
def build_primes(target):
    global primes
    if target <= primes[-1]: return
    candidate = primes[-1]
    while primes[-1] < target:
        candidate += 2
        cc = int(sqrt(candidate)+1)
        not_prime = False
        for prime in primes:
            if cc < prime:
                break
            if candidate % prime == 0:
                not_prime = True
                break
        if not not_prime: primes.append(candidate)
def is_prime(n):
    build_primes(n)
    return n in primes

if __name__=='__main__':
    build_primes(30)
    print(primes)
    for i in [1,2,3,4,5,1337]:
        print(i,is_prime(i))
