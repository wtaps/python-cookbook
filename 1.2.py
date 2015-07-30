#!/Users/tony/venv3/bin/python

record = ('Tony', 187, 150, (1, 1, 2000))

name, *_, (*_, year) = record

print(name)
print(year)
