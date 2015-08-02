#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
排序不支持原生比较的对象
"""


# 1. sorted

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

# 2. operator.attrgetter
from operator import attrgetter, itemgetter

print(sorted(users, key=attrgetter('user_id')))

