import calendar
import random

import collections

import numpy

import time

def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
if __name__ == '__main__':
    print(int(time.time()))
    print(time.ctime())
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1527150730)))
    lc=calendar.HTMLCalendar()
    lc.formatyear(2018)
    arr=numpy.random.randint(10,50,size=30)
    print(arr)
    print(sort(arr))
