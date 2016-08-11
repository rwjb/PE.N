def gen_prime():
    yield 2
    yield 3
    primes = [2,3]
    # all primes other than 2,3 can be expressed as 6k+/-1
    base, mod = 0, 1
    while True:
        if 0 < mod: base += 6
        mod *= -1
        num = base + mod
        p_cap = int(num ** 0.5)
        is_prime = True
        for p in primes:
            if p_cap < p: break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes += [num]
            yield num
s = 0
for prime in gen_prime():
    if 2000000 <= prime: break
    s += prime
print(s)
