def prob():
    for c in range(998,1,-1):
        cc = c * c
        for b in range(1000-c-1,1,-1):
            a = 1000 - b - c
            if a * a + b * b == cc:
                return a * b * c
print(prob())
