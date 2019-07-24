import prime as p

p.build_primes(9999)
offline = p.primes[:]
o = 0
while offline[o] < 1000: o += 1
offline = offline[o:-1]

anagram = dict()
for prime in offline:
    srtd = ''.join(sorted(str(prime)))
    anagram[srtd] = anagram.get(srtd,[]) + [prime]
for a in anagram:
    if len(anagram[a]) >= 3:
        ana = anagram[a]
        for i in range(len(ana)-2):
            for j in range(i+1,len(ana)-1):
                if ana[j]-ana[i] != 3330: continue
                for k in range(j+1,len(ana)):
                    if ana[k]-ana[j] == 3330:
                        print(ana[i],ana[j],ana[k])
