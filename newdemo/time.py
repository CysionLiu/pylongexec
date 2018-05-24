import calendar

import time

if __name__ == '__main__':
    print(int(time.time()))
    print(time.ctime())
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1527150730)))
    lc=calendar.HTMLCalendar()
    lc.formatyear(2018)