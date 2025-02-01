import datetime as dt

now = dt.datetime.now()
# print(type(now))
# print(now)

year = now.year
# print(type(year))
# print(year)

# if year == 2020:
#     print("Wear a face mask.")
# else:
#     print("Covid is in the past now.")

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1988, month=12, day=22, hour=7, minute=50)
print(date_of_birth)
