prod = 1
for i in range(100,0,-1):
    prod *= i
print(sum(int(i) for i in str(prod)))
