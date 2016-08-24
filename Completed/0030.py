def fifth(num):
    out = 0
    temp = num
    while temp:
        out += (temp % 10)**5
        temp = temp // 10
    return out == num

out = 0
for num in range(2,999999):
    if fifth(num):
        out += num
print(out)
