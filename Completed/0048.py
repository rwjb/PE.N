fltr = 10 ** 10
out = 0
for i in range(1,1000+1):
    out += i**i
    out = out % fltr
print(out)
