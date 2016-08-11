three    = [i for i in range(0,1000,3)]
five     = [i for i in range(0,1000,5)]
fifteen  = [i for i in range(0,1000,15)]
print(sum(three + five) - sum(fifteen))
