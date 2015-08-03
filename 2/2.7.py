#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
最短匹配模式
"""

import re


# before
text = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'\"(.*)\"')
print(str_pat.findall(text))


# after
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text))
