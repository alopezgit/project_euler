## Code for problem https://projecteuler.net/problem=19

year = 1900
month = 1
thirty_days = [4, 6, 9, 11] ## 1-12 Jan - Dec
day_week = 0 # Zero-indexed, 0-6 Monday-Sunday
n_sunday = 0
while True:
    ## Check if month is February, then if leap year
    if month == 2:
        if year % 4 == 0 and (year % 100 or year % 400 == 0):
            day_week = (day_week + 29) % 7
        else:
            ## This is not necessary, 28 % 7 = 0
            day_week = (day_week + 28) % 7
    elif month in thirty_days:
        day_week = (day_week + 30) % 7
    else:
        day_week = (day_week + 31) % 7
    
    month += 1
    if month == 13:
        month = 1
        year += 1
    if year == 2001:
        break
    if day_week == 6 and year > 1900:
        n_sunday += 1
print 'Number of sundays is {:d}'.format(n_sunday)
