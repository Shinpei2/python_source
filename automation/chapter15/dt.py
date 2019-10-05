import time, datetime
from datetime import datetime

dt1 = datetime(2019,9,8,10,35,0)
dt2 = datetime.now()
print(dt1)
print(dt2)

print(dt1.year, dt1.month, dt1.day)
print(dt1.hour, dt1.minute, dt1.second)



dt3 = datetime.fromtimestamp(100000)
dt4 = datetime.fromtimestamp(time.time())
dt5 = datetime.fromtimestamp(0)

print(dt3)
print(dt4)
print(dt5)