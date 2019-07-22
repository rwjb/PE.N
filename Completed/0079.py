# answer: 73162890
# first pass, assume digits are unique
with open("p079_sequences.txt") as f:
    triplets = [line[:-1] for line in f]
pairs = [triplet[:2] for triplet in triplets] \
      + [triplet[1:] for triplet in triplets]
nums = sorted(set(pairs))
with open("p079_seq_sort.txt",'w') as f:
    for num in nums:
        f.write("{}\n".format(num))
def verify(candidate):
    for triplet in triplets:
        c = 0
        for t in triplet:
            i = candidate[c:].find(t)
            if i < 0: return False
            c = c + i + 1
    return True
# done by hand once the sorted uniques were available
print("73162890",verify("73162890"))
