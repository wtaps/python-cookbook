#!/Users/tony/venv3/bin/python
# -*- coding: utf-8 -*-
"""
collections.deque 可以生成一个固定长度的队列，超出固定长度
会删除最前面的一个元素
"""

from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
