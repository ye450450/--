"""
import random
import time
from datetime import date



due =abs(today-d)
print(abs)
randnum=random.randint(0,abs)
print(randnum)
"""
import datetime
import random

def random_date():
    end = datetime.date.today()
    start = datetime.date(2010,1,1)
    return start + datetime.timedelta(days=random.randint(0, int((end - start).days)))

num= random_date()
print(num)

