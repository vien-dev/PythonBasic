from iteration import MyNumber

mn = MyNumber()

for nu in mn:
    print(nu)
    import traceback as tb
    import sys
    t, v, trb = sys.exc_info()
    tb.print_tb(trb)
else:
    print("it's the end of my numbers")

import hello_world

print(dir(hello_world))
import iteration
print(dir(iteration))

import json
print(dir(json))

import math
print(dir(math))

import re
import inspect as i
print(dir(re.compile))
print(i.getsource(MyNumber))
for func in i.getmembers(re, i.isfunction):
    print(func)
#print(i.getsource(re))

