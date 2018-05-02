def num_solutions(p):
    solutions = []
    for a in range(1,p/3):
        aa = a * a
        for b in range(a,(p-a)/2):
            c = p - (a+b)
            if c < b: break
            if aa + b*b == c*c:
                solutions.append((a,b,c))
    return len(solutions)
#'''
best_p, best_count = 120,3
for p in range(2,1000+1,2):
    count = num_solutions(p)
    if best_count < count:
        best_p, best_count = p, count
print(best_p)
#'''
