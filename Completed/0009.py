# pyth int triples all: mm-nn, 2mn, mm+nn, m>n
# .'. a+b+c=1000 <=> 500 = m(m+n)
# .'. ret a*b*c = 2mn(mm-nn)(mm+nn)
def foo():
    # 500 factors to 2^2 5^3
    for x in range(2+1):
        for y in range(3+1):
            m = pow(2,x)*pow(5,y)
            n = 500 / m - m
            if 0 < n < m :
                print(x,y)
                return 2*m*n*(pow(m,4)-pow(n,4))
print(foo())
