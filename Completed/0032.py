from itertools import permutations
from time import clock
'''
# First Approach
def decode(perm,filt):
    p = 0
    ret = list()
    for f in filt:
        temp = 0
        for i in range(f):
            temp += perm[p] * pow(10,i)
            p += 1
        ret += [temp]
    return ret

start = clock()
prods = set()
for p in permutations(range(1,9+1)):
    for f in [(1,4,4),(2,3,4)]:
        a,b,c = decode(p,f)
        if a * b == c:
            prods.add(c)
print(sum(prods))
end = clock()
print(end - start)
'''

start = clock()
print(sum(set(a * b for a in range(1,100) for b in range(1,9999 // a) if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789')))
end = clock()
print(end - start)
