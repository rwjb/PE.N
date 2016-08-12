def fibb():
    yield 0
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a
check = 10**999
for i, f in enumerate(fibb()):
    if f >= check:
        print(i)
        break
