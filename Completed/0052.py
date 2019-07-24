def is_6permute(n):
    bag = sorted(str(n))
    for m in range(2*n,6*n+1,n):
        if sorted(str(m)) != bag:
            return False
    return True

# first digit must be 1, higher and *6 increases number of digits
# minimum 6 digits

i = 100000
while not is_6permute(i): i += 1
print(i)
