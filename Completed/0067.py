f = open("p067_triangle.txt")
nums = [[int(token) for token in line.split()] for line in f]
f.close()

for row in range(len(nums)-2,-1,-1):
    for col in range(len(nums[row])):
        nums[row][col] += max(nums[row+1][col],nums[row+1][col+1])
print(nums[0][0])
