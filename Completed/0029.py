out = set()
for i in range(2,100+1):
    for j in range(2,100+1):
        out.add(i**j)
print(len(out))
