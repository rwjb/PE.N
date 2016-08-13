def divisors(num):
    cap = int(num ** .5)
    out = []
    for i in range(1,cap+1):
        if not num % i:
            out += [i]
            if i * i != num and i != 1: out += [num // i]
    return out
def gen_amicable_pair(num):
    test = sum(divisors(num))
    if test != num and num == sum(divisors(test)):
        return num, test
    return [0]
out = set()
for i in range(2,10000):
    if i in out: continue
    for n in gen_amicable_pair(i):
        out.add(n)
print(sum(out))
    
