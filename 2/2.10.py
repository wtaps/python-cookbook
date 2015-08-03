#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
在正则式中使用Unicode
"""

import re

num = re.compile('\d+')
# ASCII digits
num.match('123')
# Arabic digits
num.match('\u0661\u0662\u0663')


arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
