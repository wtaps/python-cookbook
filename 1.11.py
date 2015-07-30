#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
命名切片
"""


# before
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37]))

# after
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES] * float(record[PRICE])

