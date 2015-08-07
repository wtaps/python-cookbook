#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
二八十六进制整数
"""


>>> x = 1234
>>> bin(x)
'0b10011010010'
>>> oct(x)
'0o2322'
>>> hex(x)
'0x4d2'
>>>

# 不显示 0b 0o 0x
>>> format(x, 'b')
'10011010010'
>>> format(x, 'o')
'2322'
>>> format(x, 'x')
'4d2'
>>>
