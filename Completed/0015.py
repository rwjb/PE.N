storage = [[0] * 21] * 21
for x in range(21):
    for y in range(21):
        if not x or not y: storage[x][y] = 1
        else:
            storage[x][y] = storage[x-1][y] + storage[x][y-1]
print(storage[20][20])
