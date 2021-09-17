from datetime import date, timedelta, datetime

today = date.today()
yesterday = today - timedelta(days =1)
month_ago = today - timedelta(days =30)
print(yesterday)
print(today)
print(month_ago)

data_string = "01/01/25 12:10:03.234567"
data_dt = datetime.strptime(data_string, "%d/%m/%y %H:%M:%S.%f")
print(data_dt)