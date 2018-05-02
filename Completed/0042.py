tri_nums = [1]
def build_tri(target):
    global tri_nums
    while tri_nums[-1] < target:
        n = len(tri_nums) + 1
        tri_nums.append(n*(n+1)//2)
def is_tri(n):
    build_tri(n)
    return n in tri_nums
def word_value(word):
    return sum(ord(letter) - 64 for letter in word)
with open("p042_words.txt") as f:
    line = f.readline()
words = line.split(',')
words = [word[1:-1] for word in words]
print(sum(is_tri(word_value(word)) for word in words))
