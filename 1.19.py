#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
转换并同时计算数据
"""


nums = [1, 2, 3, 4, 5]
s = sum((x * x for x in nums))
s = sum(x * x for x in nums) # 更优雅


