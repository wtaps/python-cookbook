#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
序列中出现次数最多的元素
"""


from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words) # 计算次数
top_three = word_counts.most_common(3) # 出现频率最高的3个单词
print(top_three)
