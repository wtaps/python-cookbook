#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
合并多个字典或映射
"""


from collections import ChainMap

a = {'x': 1, 'y': 2}
b = {'y': 1, 'z': 2}

c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])

merged = dict(b)
merged.update(a)
print(merged)
