def is_palindrome(num):
    num = str(num)
    if len(num) < 2: return True
    if num[0] == num[-1]:
        return is_palindrome(num[1:-1])
    return False
def test():
    for i in range(999,900,-1):
        for j in range(i,900,-1):
            temp = i * j
            if is_palindrome(temp):
                return temp
print(test())
                
