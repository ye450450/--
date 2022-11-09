import time
from datetime import date

today = date.today()
print(today)

Bday= date(today.year+1,8,18)
print(Bday)

due = abs(Bday-today)
print (due)
