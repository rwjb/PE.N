import prime as p
for i in range(9,10000,2):
    if p.is_prime(i): continue
    for d in (2*s*s for s in range(1,int(i**0.5))):
        if p.is_prime(i-d):
            break
    else:
        print(i)
        exit(0)
