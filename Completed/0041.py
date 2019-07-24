from prime import is_prime
from itertools import permutations

# pandigital nums len 8 or 9 always divisible by 3 (sums are multiples of 9)
for pandigital in permutations('7654321'):
    if pandigital[-1] in [2,4,5,6]: continue
    if is_prime(int(''.join(pandigital))):
        print(''.join(pandigital))
        break
