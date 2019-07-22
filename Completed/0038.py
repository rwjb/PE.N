def is_pandigital(n):
    return ''.join(sorted(list(str(n)))) == '123456789'
def gen(n):
    out = ""
    i = 0
    while len(out) < 9:
        i += 1
        out = out + str(n * i)
    return int(out) if len(out) == 9 else None

biggest = 0
for i in range(1,9999+1): # 5 digit numbers can't produce 9digit candidates
    if str(i)[0]!='9': continue # number to beat starts with 9
    candidate = gen(i)
    if candidate == None: continue
    if biggest < candidate and is_pandigital(candidate):
        biggest = candidate
print(biggest)
