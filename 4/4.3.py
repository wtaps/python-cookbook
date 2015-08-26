#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
使用生成器创建新的迭代模式
"""


def frange(start, stop, increment):
    x = start
    while x <= stop:
        yield x
        x += increment


n = frange(1, 5, 1)
for i in n:
    print(i)
