import prime as p
limit = pow(10,6)-1
p.build_primes(limit)
offline = p.primes[:]
print(len(offline))
n = 21
tail_sum = sum(offline[-n:])
while tail_sum > limit:
    tail_sum -= offline.pop()
    tail_sum += offline[-n]

print(len(offline))

sums = [sum(offline)]
band = len(offline)

while band:
    for s in sums:
        if s > limit: break
        if p.is_prime(s):
            print(s,sums.index(s),band)
            exit(0)
    old_sums = sums
    band -= 1
    sums = [old_sums[0]-offline[band]]
    for e,os in enumerate(old_sums):
        sums.append(os-offline[e])
    del old_sums

'''
ans = None
largest_band = 20
for i in range(len(offline)):
    if len(offline) - i < largest_band:
        break
    s = None
    for j in range(i+largest_band,len(offline)):
        if not s: s = sum(offline[i:j])
        else: s += offline[j-1]
        if s > limit: break
        if p.is_prime(s):
            largest_band = j - i
            ans = s
print(ans)
'''
