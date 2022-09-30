from datetime import datetime, timedelta

try:
    print('Input birth date in format DD.MM.YYYY HH:ММ')
    s_date = datetime.strptime(input(), "%d.%m.%Y %H:%M")
except Exception:
    print('ERROR! Input date in format DD.MM.YYYY')
    exit()
time_10d = s_date + timedelta(days=10000)
time_1000m = s_date + timedelta(minutes=1000000)
time_1000000s = s_date + timedelta(seconds=1000000000)
print(time_10d)
print(time_1000m)
print(time_1000000s)