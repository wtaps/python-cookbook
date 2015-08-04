#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
合并拼接字符串
"""


parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
#'Is Chicago Not Chicago?'
print(','.join(parts))
#'Is,Chicago,Not,Chicago?'
print(''.join(parts))
#'IsChicagoNotChicago?'


a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
#'Is Chicago Not Chicago?'


print('{} {}'.format(a,b))
#'Is Chicago Not Chicago?'
print(a + ' ' + b)
#'Is Chicago Not Chicago?'


a = 'Hello' 'World'
print(a)
#'HelloWorld'


data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
#'ACME,50,91.1'

c = 'Hello PC'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

# 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
