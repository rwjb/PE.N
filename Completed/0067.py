# 0018.py, This Time You Can't Brute Force
with open("p067_triangle.txt") as f:
    nums = [ [int(token) for token in line.split()] for line in f ]

for row in range(len(nums)-2,-1,-1):
    for col in range(len(nums[row])):
        nums[row][col] += max(nums[row+1][col],nums[row+1][col+1])
print(nums[0][0])
