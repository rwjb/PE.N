#num = 13195
num = 600851475143
max_factor = 2
while num % 2 == 0:
    num /= 2
div = 3
while num != 1:
    while num % div == 0:
        max_factor = div
        num /= div
    div += 2
print(max_factor)
