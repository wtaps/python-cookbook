#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
查找两个字典相同点
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'x': 11,
    'y': 2,
    'w': 3,
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
