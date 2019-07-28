''' # test matrix
mtrx = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,903,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331],
]
'''

mtrx = []
with open("p081_matrix.txt") as f:
    mtrx = [[int(token) for token in line.strip().split(',')] for line in f]

side = len(mtrx)
mtrx = [[10**9]*side] + mtrx
for e,m in enumerate(mtrx):
    mtrx[e] = [10**9] + m
mtrx[0][0] = mtrx[0][1] = mtrx[1][0] = 0

for i in range(1,side+1):
    for j in range(1,side+1):
        top = mtrx[i-1][j]
        lft = mtrx[i][j-1]
        mtrx[i][j] += min(top,lft)
print(mtrx[side][side])
