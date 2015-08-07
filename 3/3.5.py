#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字节到大整数的打包与解包
"""


data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

>>> len(data)
16
>>> int.from_bytes(data, 'little')
69120565665751139577663547927094891008
>>> int.from_bytes(data, 'big')
94522842520747284487117727783387188
>>>

>>> x = 94522842520747284487117727783387188
>>> x.to_bytes(16, 'big')
b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
>>> x.to_bytes(16, 'little')
b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'
>>>
