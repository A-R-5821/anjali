# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date of one week from the date entered
from _datetime import datetime,timedelta
print("Today's date is")
print(datetime.now().date())
one_day = timedelta(days=1)
Today=datetime.now()
yesterday = Today - one_day
print("date of yesterday is:")
print(yesterday.date())
one_week = timedelta(weeks=1)
next_week = Today + one_week
print("Next week is")
print(next_week)
