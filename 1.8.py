#!/Users/tony/venv3/bin/python
# -*- coding: utf-8 -*-
"""
字典运算
"""

prices = {
    'HP': 45.23,
    'IBM': 12.42,
    'APPLE': 2343,
    'DELL': 154.12,
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
