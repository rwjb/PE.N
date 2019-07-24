bag1 = set([1])
bag89 = set([89])

square = dict(zip([str(i) for i in range(9+1)],[i*i for i in range(9+1)]))

cnt = 0
for i in range(1,10**7):
    bag = set([i])
    while i not in bag1 and i not in bag89:
        i = sum(square[c] for c in str(i))
        bag.add(i)
    if i in bag1: bag1.update(bag)
    else: bag89.update(bag)
print(len(list(filter(lambda x: x < 10**7,bag89))))
