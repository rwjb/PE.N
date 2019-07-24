euler = [2]
for i in range(1,33+1): euler += [1,2*i,1]

def numerator(n):
    h1 = 0
    h  = 1
    for i in range(n):
        h2, h1 = h1, h
        h = euler[i] * h1 + h2
    return h

print( sum( int(c) for c in str(numerator(100)) ) )
