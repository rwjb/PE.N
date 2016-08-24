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
p = Primes()
highest_n, ab = 0, 0
for a in range(-999,999+1):
    for b in range(-1000,1000+1):
        n = 0
        while p.is_prime(n * n + a * n + b): n += 1
        if highest_n < n:
            highest_n = n
            ab = a * b
print(ab)
