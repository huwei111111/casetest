import hashlib
import hmac
import time
import datetime
import pandas as pd


def mis_md5():
    sign = '9be9bc14b1a878cc3f4a63e442c52a336a2c796030c814f8fede67537c8b875e'


def last_time_yyymmdd(n):
    later_oneday = (datetime.datetime.now() + datetime.timedelta(days=n)).strftime("%Y-%m-%d %H:%M:%S")
    times = pd.to_datetime(later_oneday).strftime('%Y-%m-%d ')
    print(times)
    return times


def last_time(n):
    """获取当前时间n前后的时间"""
    time_one = (datetime.datetime.now() + datetime.timedelta(days=n)).strftime('%Y-%m-%d')
    return time_one


print(last_time(6))

s = (datetime.datetime.now()+datetime.timedelta(days=4)).strftime('%y-%m-%d %H:%M:%d')
print(s)
