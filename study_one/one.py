# @File  : one.py
# @Author: 521
# @Time: 2023/8/27 18:59 
# -*- coding: utf-8 -*-
import re
phone = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
print(phone)
mo = phone.search('my number is 123-232-2223')
print(mo)
print('phone number found:' + mo.group())

heroregex = re.compile(r'batman|tina fey')
mo1 = heroregex.search('batman and tina fey')
print(mo1)
print(mo1.group())

bat = re.compile(r'bat(wo)?man')
mo1 = bat.search('my bat is batmam')
mo2 = bat.search('batwoman')
# print(mo1)
# print(mo1.group())
print(mo2.group())
