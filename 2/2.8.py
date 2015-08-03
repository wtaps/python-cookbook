#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
最短匹配模式
"""

import re


comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is 
a comment */'''

print(comment.findall(text1))
print(comment.findall(text2))


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))


comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
