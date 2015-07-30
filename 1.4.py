#!/Users/tony/venv3/bin/python
# -*- coding: utf-8 -*-

from heapq import nlargest, nsmallest

record = [1, 2, 2, 4, 0, 9, 10, 6, 9, 3, 6, 7, 8, 9, 3, 6, 1, 0, 8, 0, 7, 6]

def findmin(record):
    l = []
    small = min(record)
    num = record.count(small)

    for i in range(num):
        l.append(small)

    return l
        
def findmax(record):
    l = []
    small = max(record)
    num = record.count(small)

    for i in range(num):
        l.append(small)

    return l

if __name__ == '__main__':
    print(findmin(record))
    print(findmax(record))
    print(nlargest(3, record))
    print(nsmallest(3, record))
