# below takes <2s
from itertools import permutations
divs = [3,5,7,11,13,17]
total = 0
for p in permutations('0123456789'):
    if p[0] in '0': continue # pandigital property lost
    if p[3] not in '02468': continue # d_4 div 2
    if p[5] not in '05': continue # d_6 div 5
    n = ''.join(p)
    frags = [n[i:i+3] for i in range(2,7+1)]
    for div,frag in zip(divs,frags):
        if int(frag) % div != 0:
            break
    else:
        total += int(n)
print(total)
