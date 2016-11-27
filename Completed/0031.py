# coins = {200:1,100:2,50:4,20:10,10:20,5:40,2:100,1:200}
coins = (200,100, 50,20,10 ,5,2)
amt   = (0,0 ,0,0,0 ,0,0)

class Stack():
    def __init__(self):
        self.data = []
        self.mark = set()
    def push(self,i):
        if i in self.mark: return
        self.data.append(i)
        self.mark.add(i)
    def pop(self):
        return self.data.pop()
    def peak(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)

ans = set()
s = Stack()
s.push(amt)
count = 0
while len(s):
    look = s.pop()
    ans.add(look)
    val = 200 - sum(coin * freq for coin, freq in zip(coins, look))
    for i in range(7):
        if val >= coins[i]:
            temp = list(look)
            temp[i] += 1
            s.push(tuple(temp))

print(len(ans)) # 73682
