def palin(pal):
    pal = str(pal)
    if len(pal) <= 1: return True
    return palin(pal[1:-1]) if pal[0] == pal[-1] else False



out = 0
for i in range(1,1000000,2):
    if palin(i) and palin(bin(i)[2:]):
        out += i
print(out)
