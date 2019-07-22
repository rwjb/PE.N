def is_palindrome(num):
    num = str(num)
    l = len(num)
    for i in range(l//2):
        if num[i]!=num[l-1-i]: return False
    return True
def test():
    for i in range(999,900,-1):
        for j in range(i,900,-1):
            temp = i * j
            if is_palindrome(temp):
                return temp
print(test())
