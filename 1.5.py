#!/Users/tony/venv3/bin/python
# -*- coding: utf-8 -*-

from heapq import heappush, heappop


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heappop(self._queue)[-1]

    
class Item(object):
    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('goo'), 5)
q.push(Item('sad'), 2)
q.push(Item('gdh'), 1)
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
print(q._queue)
print(q.pop())
