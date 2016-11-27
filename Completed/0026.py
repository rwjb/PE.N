def div_digit(div):
    num = 1 * 10
    mem = dict()
    while mem.get(num, False) == False:
        mem[num] = num % div * 10
        num = mem[num]
        if num == 0: return 0
    track, count = mem[num], 1
    while num != track:
        track = mem[track]
        count += 1
    return count
print(max([i for i in range(2,1000)], key=div_digit))
