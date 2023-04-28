from collections import namedtuple
import sys


Student = namedtuple('Student', ('name', 'mark'))

print(sorted([Student(name=_name, mark=int(_mark)) for line in sys.stdin for _name, _mark in [line.rstrip().split()]], key=lambda x: x.mark)[1].name)
