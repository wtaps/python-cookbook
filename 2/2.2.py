#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字符串开头或结尾匹配
"""


filename = 'spam.txt'
filename.startswith('spam')
filename.endswith('txt')



def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(choices) # wrong
url.startswith(tuple(choices)) # right
