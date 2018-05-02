# answer: 73162890
with open("p079_sequences.txt") as f:
    nums = [int(line) for line in f]
nums = list(set(nums))
nums.sort()
with open("p079_seq_sort.txt",'w') as f:
    for num in nums:
        f.write("{}\n".format(num))
# done by hand once the sorted uniques were available
