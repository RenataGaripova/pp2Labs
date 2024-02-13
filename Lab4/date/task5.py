import datetime
from math import fabs

day1, month1, year1, hour1, min1, sec1 = map(int, input().split())
day2, month2, year2, hour2, min2, sec2 = map(int, input().split())

date1 = datetime.datetime(day=day1, month=month1, year=year1, hour=hour1, minute=min1, second=sec1)
date2 = datetime.datetime(day=day2, month=month2, year=year2, hour=hour2, minute=min2, second=sec2)

diff = date1 - date2
diff_seconds = diff.total_seconds()

print(f"The difference is {fabs(diff_seconds)} seconds.")