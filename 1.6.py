#!/Users/tony/venv3/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(1)
d['c'].append(1)
d['d'].append(1)

print(d)

for k, v in d.items():
    print(k, v)


# before
"""
d = {}
for key, value in paris:
    if key not in d:
        d[key] = []
    d[key].append(value)
"""
# after
"""
d = defaultdict(list)
for key, value in paris:
    d[key].append(value)
"""
