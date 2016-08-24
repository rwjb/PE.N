class Primes:
    def __init__(self):
        self.p_list = [2,3]
        self.primes = set(self.p_list)
        self.high = 3

        self.base = 0
        self.mod  = 1
    def is_prime(self, num):
        while True:
            if num in self.primes: return True
            if num < self.high: return False
            self.high = self.calc_primes()
    def calc_primes(self):
        # all primes other than 2,3 can be expressed as 6k+/-1
        while True:
            if 0 < self.mod: self.base += 6
            self.mod *= -1
            num = self.base + self.mod
            p_cap = int(num ** 0.5)
            is_prime = True
            for p in self.p_list:
                if p_cap < p: break
                if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.add(num)
                self.p_list.append(num)
                return num

circular_nums = [set([2,5])]
for c in range(1000000):
    hold = set()
    char = str(c)
    valid = True
    for i in range(len(char)):
        if char[i] in ['0','2','4','5','6','8']:
            valid = False
            break
        num = int(char[i:] + char[:i])
        hold.add(num)
    if valid:
        circular_nums.append(hold)

p = Primes()
circular_primes = set()
for nums in circular_nums:
    all_prime = True
    for num in nums:
        if not p.is_prime(num):
            all_prime = False
            break
    if all_prime: circular_primes.update(nums)

print(len(circular_primes))
