import datetime

today_date = datetime.datetime.now()
difference = datetime.timedelta(days = 5) 

res = today_date - difference

print(res)