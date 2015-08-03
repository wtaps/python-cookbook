#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
使用多个界定符分割字符串
"""


import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
new_line = re.split(r'[;,\s]\s*', line)
print(new_line)
