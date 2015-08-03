#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字符串匹配和搜索
"""

import re


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
re.match(r'\d+/\d+/\d+', text1)

datepat = re.compile(r'\d+/\d+/\d+')
datepat.match(text1)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

for m in datepat.finditer(text):
    print(m.groups())
