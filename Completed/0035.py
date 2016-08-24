from time import time
def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

start = time()
primes = set(rwh_primes2(1000000))
print(time() - start)

start = time()
circular_nums = [set([2,5])]
for c in primes:
    hold = set()
    char = str(c)
    skip = False
    for i in char:
        if i in ['0','2','4','5','6','8']:
            skip = True
            break
    if skip: continue
    for i in range(len(char)):
        hold.add(int(char[i:] + char[:i]))
    circular_nums.append(hold)
print(time() - start)

start = time()
circular_primes = set()
for nums in circular_nums:
    all_prime = True
    for num in nums:
        if num not in primes:
            all_prime = False
            break
    if all_prime: circular_primes.update(nums)
print(time() - start)

print(len(circular_primes))
