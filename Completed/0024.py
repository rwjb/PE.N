import itertools
j = 1
out = ""
for c in list(itertools.islice(itertools.permutations(range(10)), 999999, 999999+1))[0]: out += str(c)
print(out)
