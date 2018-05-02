# digits[len] = freq
#   digits[1] = 9 (1-9)
#   digits[2] = 90 (10-99)
digits = dict()
for i in range(1,8):
    digits[i] = pow(10,i) - pow(10,i-1)
def nth_digit(n):
    for i in range(1,10):
        if n <= digits[i]*i:
            start = pow(10,i-1)
            break
        n -= digits[i]*i
    # have span=(10,99), i=2, n=digit in that sequence from 0, d=digit of num
    n, d = (n-1) // i, (n-1) % i
    return int(str(start + n)[d])
    #return span,i,n,d

out = 1
for i in range(7):
    out *= nth_digit(pow(10,i))
print(out)
