#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字符串搜索和替换
"""

import re


text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
