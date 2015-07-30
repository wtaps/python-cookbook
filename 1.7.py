#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
字典排序
"""

import json
from collections import OrderedDict

# before
d = {}
d['azog'] = 1
d['anson'] = 2
d['bili'] = 3
print(d)
print(json.dumps(d))

# after
d = OrderedDict()
d['azog'] = 1
d['anson'] = 2
d['bili'] = 3
print(d)
print(json.dumps(d))
