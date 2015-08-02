#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
映射名称到序列元素
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('tony@gmail.com', '2012-12-12')
print(sub)
print(sub.addr)
print(sub.joined)


# before
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# after
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost_new(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
    total += s.shares * s.price
    return total
