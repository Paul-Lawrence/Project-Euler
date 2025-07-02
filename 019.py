months = {'J': 31, 'F': 28, 'Ma': 31, 'A': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'S': 30, 'O': 31, 'N': 30, 'D': 31}
bad_years = [x for x in range(1900, 2000, 100) if x%400 != 0]
print(bad_years)
sunday_count = 0
day = 2
for year in range(1901, 2001):
    for month in months:
        day += months[month]
        if (year%4 == 0) and (year not in bad_years):
            if month == 'F':
                day += 1
        if day%7 == 0:
            sunday_count += 1
print(sunday_count)