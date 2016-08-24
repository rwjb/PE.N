n = 1
step = 2
total = 1
fin = 1001**2
while n < fin:
    for _ in range(4):
        n += step
        total += n
    step += 2
print(total)
