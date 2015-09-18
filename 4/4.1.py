#!/usr/local/bin/python3.3
# -*- coding: utf-8 -*-
"""
手动遍历迭代器
"""


def manual_iter():
    with open('/etc/hosts') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass



if __name__ == '__main__':
    manual_iter()
