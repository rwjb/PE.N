a, b, c = 0, 1, 1
s = 0
while a <= 4000000:
    s += a
    a, b, c = b + c, b + 2 * c, 2 * b + 3 * c
print(s)
