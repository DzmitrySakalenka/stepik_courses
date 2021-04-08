import datetime as dt


year, month, day = map(int, input().split())
dd = dt.date(year, month, day)

delta = dt.timedelta(days=int(input()))
dd += delta

print(dd.year, dd.month, dd.day)