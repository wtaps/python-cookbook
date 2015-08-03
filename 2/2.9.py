#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
将Unicode文本标准化
"""

import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1 == s2)


t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
