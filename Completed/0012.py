def divisors(num):
    cap = int(num ** .5)
    out = sum(2 for i in range(1,cap+1) if not num % i)
    if cap * cap == num: out -= 1
    return out
i = 1
num = 0
count = 0
while count <= 500:
    num += i
    i += 1
    count = divisors(num)
print(num)
