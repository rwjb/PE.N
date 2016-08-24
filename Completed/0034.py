def fact(num):
    if num==0: return 1
    out = num
    for i in range(2,num):
        out *= i
    return out
digit_to_f = {}
for i in range(10): digit_to_f[i] = fact(i)

def curious(num):
    tot = 0
    tmp = num
    while tmp:
        tot += digit_to_f[tmp % 10]
        tmp = tmp // 10
    return tot == num

out = []
for i in range(3,999999):
    if curious(i):
        out.append(i)
print(out)
print(sum(out))
