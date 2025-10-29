import os
os.system('cls' if os.name == 'nt' else 'clear')
from datetime import datetime

now = datetime.now()
print(now)

day = now.day
print(day)

month  = now.month
print(month)

year = now.year
print(year)

hour = int((now.hour) - 12)
print(hour)

minute = now.minute
print(minute)

print(f'It is {day}-{month}-{year}')
print(f'The time is {hour}:{minute}')

new_year = datetime(2026,1,1)
print(new_year)

day = new_year.day
print(day)

month = new_year.month
print(month)

year = new_year.year
print(year)

hour = new_year.hour
print(hour)

minute = new_year.minute
print(minute)


# Formatting date time using strftime method

t = now.strftime("%H:%M:%S")
print("time:", t)

time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)

today = now.strftime("%A")
print(f"its {today}")

# String to Time Using strptime

date_string = "29 October 2025"
print('date_string = ', date_string)
date_object = datetime.strptime(date_string, "%d %B %Y")
print("date_object = ", date_object)

# Difference Between Two Points in Time Using
from datetime import date
today = date(year=2025, month=10, day=29)
new_year = date(year=2026, month=1, day=1)

time_left = new_year - today
print('Time left for new year: ', time_left)

t1 = datetime(year=2025, month=10, day=29, hour = now.hour, minute = now.minute, second = now.second)
t2 = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

