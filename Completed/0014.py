def coll(n):
    yield n
    while n != 1:
        if n % 2 == 0: n = n / 2
        else:          n = 3 * n + 1
        yield n
'''
# brute forced
j, big = 0, 0
for i in range(1,1000000):
    temp = len(list(coll(i)))
    if temp > big:
        j = i
        big = temp
print(j)
'''
# memory
class Link:
    def __init__(self,nxt=None):
        self.next = nxt
        self.size = None
    def get_size(self):
        if not self.size:
            if not self.next:
                self.size = 1
            else:
                self.size = self.next.get_size() + 1
        return self.size
d = {}
for i in range(1,1000000):
    if i in d: continue
    hold = None
    for j in coll(i):
        if j in d:
            if hold: hold.next = d[j]
            break
        d[j] = Link()
        if hold: hold.next = d[j]
        hold = d[j]
big_len, big_num = 0, 0
for num in range(1,1000000):
    temp = d[num].get_size()
    if big_len < temp:
        big_len = temp
        big_num = num
print(big_num)
