#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
用Shell通配符匹配字符串
"""


from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))
