from math import sqrt
def num_solutions(p):
    solutions = []
    for a in range(1,p):
        aa = a * a
        for b in range(a,p):
            c = p - (a+b)
            if c < b: continue
            if aa + b*b == c*c:
                solutions.append((a,b,c))
    return len(solutions)
#'''
best_p, best_count = 120,3
for p in range(1,1000+1):
    count = num_solutions(p)
    if best_count < count:
        best_p, best_count = p, count
print(best_p)
#'''
