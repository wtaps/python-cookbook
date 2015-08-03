#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
删除字符串中不需要的字符
"""

>>> # Whitespace stripping
>>> s = ' hello world \n'
>>> s.strip()
'hello world'
>>> s.lstrip()
'hello world \n'
>>> s.rstrip()
' hello world'

>>> # Character stripping
>>> t = '-----hello====='
>>> t.lstrip('-')
'hello====='
>>> t.strip('-=')
'hello'

>>> s = ' hello     world \n'
>>> s = s.strip()
>>> s
'hello     world'

>>> s.replace(' ', '')
'helloworld'
>>> import re
>>> re.sub('\s+', ' ', s)
'hello world'
