out = []
weekday = 1 # sunday = 0
weekday += sum([31,28,31,30,31,30,31,31,30,31,30,31])
for year in range(1901,2001):
    feb = 28
    if year % 4 == 0: feb = 29
    for month in [31,feb,31,30,31,30,31,31,30,31,30,31]:
        out += [weekday]
        weekday += month
out = [i % 7 for i in out]
out = [1 if i==0 else 0 for i in out]
print(sum(out))
