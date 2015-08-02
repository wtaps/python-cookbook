#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
删除序列中相同元素并保持顺序
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dedupe([1, 3, 3, 4, 9, 2, 1, 1, 10])))

def dedupe1(items, key=None):
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        print(value)
        if value not in seen:
            yield item
            seen.add(value)

a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe1(a, key=lambda d: (d['x'], d['y']))))
