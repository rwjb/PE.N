end = 2500

def is_penta(n):
    p = ( (24 * n + 1) ** 0.5 + 1 ) / 6
    return p == round(p)

ii = 1
for i in range(1,end):
    ii += 3 * i + 1
    jj = ii
    for j in range(i+1,end):
        jj += 3 * j + 1
        if is_penta(ii+jj) and is_penta(jj-ii):
            print(jj-ii)
