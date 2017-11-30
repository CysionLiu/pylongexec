import calendar
import time

from samples.constants import DIV

print(time.time())
print(time.ctime())
print(time.ctime(1512029376))
print(DIV)
for i in range(1,13):
    calendar.prmonth(2017,i)