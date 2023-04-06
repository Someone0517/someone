from datetime import date

y = int(input())
m = int(input())
d = int(input())

print(date(y, m, d).timetuple().tm_yday)