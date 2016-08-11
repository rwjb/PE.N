def difference(n):
    sum_squares = 0
    square_sum  = 0
    for i in range(1,n+1):
        sum_squares += i*i
        square_sum  += i
    square_sum *= square_sum
    return square_sum - sum_squares
#print(difference(10))
print(difference(100))
