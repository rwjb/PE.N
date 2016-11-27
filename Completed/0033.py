fractions = [(a,b) for a in range(11,99+1) for b in range(a+1,99+1)
 if a%10==b//10 or a//10==b%10]
num, den = 1, 1
for a,b in fractions:
    c,d = (a//10, b%10) if a%10==b//10 else (a%10, b//10)
    if a * d == b * c:
        num *= c
        den *= d
def gcd(a,b):
    if a == b: return a
    if a > b: return gcd(a-b,b)
    return gcd(a,b-a)
d = gcd(num,den)
while d != 1:
    num //= d
    den //= d
    d = gcd(num,den)
print(den)
