mx = 0
for a in range(100):
    for b in range(100):
        ds = sum( int(c) for c in str(a**b) )
        mx = max(ds,mx)
print(mx)
