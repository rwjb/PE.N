def divisors(num):
    if num <= 1: return []
    out = [1]
    sqrt = int(num**0.5)
    for i in range(2,sqrt+1):
        if num % i == 0:
            out.append(i)
            if num / i != sqrt: out.append(num // i)
    out.sort()
    return out
def abundant(num):
    return sum(divisors(num)) > num

abun = [i for i in range(28123+1) if abundant(i)]
nums = set(range(28123+1))
for i in range(len(abun)):
    for j in range(i,len(abun)):
        nums.discard(abun[i]+abun[j])
print(sum(nums))
