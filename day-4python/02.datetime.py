import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
print("Current date only:", datetime.date.today())

da = datetime.date(2023, 10, 4)
print("Specific date:", da)

t = datetime.time(10, 30, 45)
print("Specific time:", t)

print('Year:', now.year)
print('Month:', now.month)
print('Day:', now.day)
print('Hour:', now.hour)
print('Minute:', now.minute)
print('Second:', now.second)

# Format date (strftime)
#converying Date objects to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# %Y - Year
# %m - Month
# %d - Day
# %H - Hour (24-hour format)
# %M - Minute
# %S - Second

##parse string to date (strptime)
date_str = "2023-10-04 "
date_obj = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
print("Parsed date:", date_obj)
