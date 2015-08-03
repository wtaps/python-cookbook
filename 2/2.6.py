#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字符串忽略大小写的搜索替换
"""

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall(r'PYTHON', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

