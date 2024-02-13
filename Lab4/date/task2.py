import datetime

today_date = datetime.datetime.now()
difference = datetime.timedelta(days = 1)

yest_date = today_date - difference
tomorrow_date = today_date + difference

print(f"Yesterday it was {yest_date.strftime("%x")}.\nToday it is {today_date.strftime("%x")}.\nTomorrow it will be {tomorrow_date.strftime("%x")}.")