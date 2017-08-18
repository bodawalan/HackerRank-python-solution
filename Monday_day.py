import datetime

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
today = datetime.date(year, month, day)


print(today - datetime.timedelta(days=today.weekday(), weeks=0))
