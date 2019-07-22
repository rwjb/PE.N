# linear solution, something closer to constant possible?
Dones = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
Dteens = {0:3,1:6,2:6,3:8,4:8,5:7,6:7,7:9,8:8,9:8}
Dtens = {0:0,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
def written_form(num):
    out = 0
    ones = num % 10
    tens = num // 10 % 10
    hund = num // 100 % 10
    thou = num // 1000 % 10
    if thou: out += Dones[thou] + 8 #"thousand "
    if hund: out += Dones[hund] + 7 #"hundred "
    if hund and (tens or ones): out += 3 #"and "
    if tens == 1:
        out += Dteens[ones]
    else:
        out += Dtens[tens] + Dones[ones]
    return out
count = 0
for i in range(1,1000+1):
    count += written_form(i)
print(count)
