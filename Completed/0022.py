f = open("p022_names.txt")
names = [name for line in f for name in line.replace('"','').split(',')]
f.close()
names = sorted(names)

def alpha_value(name):
    out = 0
    for c in name: out += ord(c) - 64
    return out

out = 0
for i in range(len(names)):
    out += alpha_value(names[i]) * (i + 1)
print(out)
