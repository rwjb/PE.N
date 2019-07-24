count = 0
with open("p089_roman.txt") as f:
    for line in f:
        for rmn in ['IIII','XXXX','CCCC','VIIII','LXXXX','DCCCC']:
            count += line.count(rmn)*(6-len(rmn))
print(count)
exit(0)

numerals = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
def roman_to_int(txt):
    numeric = [numerals[t] for t in txt[::-1]]
    last = 0
    for i in range(len(numeric)):
        if last > numeric[i]: numeric[i] = -numeric[i]
        last = numeric[i]
    return sum(numeric)
def int_to_roman(i):
    numeric = []
    for rmn in sorted(numerals,key=lambda n: numerals[n],reverse=True):
        num = numerals[rmn]
        while num <= i:
            i -= num
            numeric.append(rmn)
    return ''.join(numeric)

count = 0
with open("p089_roman.txt") as f:
    for line in f:
        line = line.strip()
        count += len(line) - len(int_to_roman(roman_to_int(line)))
print(count)
