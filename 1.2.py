#!/usr/local/bin/python3.3

record = ('Tony', 187, 150, (1, 1, 2000))

name, *_, (*_, year) = record

print(name)
print(year)
