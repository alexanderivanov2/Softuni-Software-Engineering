import datetime
from datetime import timedelta
date_entry = input()
birthDay = datetime.datetime.strptime(date_entry, '%d-%m-%Y')
result = birthDay + timedelta(days=1000)
print(result.strftime("%d-%m-%Y"))
