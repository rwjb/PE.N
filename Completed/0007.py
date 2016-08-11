def gen_prime():
    yield 2
    primes = [2]
    num = 1
    while True:
        is_prime = True
        num += 2
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes += [num]
            yield num
from itertools import islice
print(next(islice(gen_prime(), 6-1, 6)))
print(next(islice(gen_prime(), 10001-1, 10001)))
