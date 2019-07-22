out = 0
weekday = 1 # sunday = 0
weekday += sum([3,0,3,2,3,2,3,3,2,3,2,3])
while weekday > 0: weekday -= 7
for year in range(1901,2000+1):
    feb = 0 if year % 4 else 1
    for month in [3,feb,3,2,3,2,3,3,2,3,2,3]:
        if weekday == 0: out += 1
        weekday += month
        if weekday > 0: weekday -= 7
print(out)
