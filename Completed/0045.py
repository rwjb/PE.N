#a(a+1)/2 = b(3b-1)/2 = c(2c-1)
#a(a+1) = b(3b-1) = 2c(2c-1)
#aa+a = 3bb - b = 4cc-2c

b = list()
c = list()
for r in range(143+1,100000+1):
    rr = r * r
    b.append(3*rr -   r)
    c.append(4*rr - 2*r)
print(list(set(b) & set(c))[0]/2)
