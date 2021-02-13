oneline_string = "Hello Vien"
multiline_string = """Hello Vien
Here is a demo multiline string
Bye Vien.
"""

import re

mo1 = re.search("(?P<name>Vien)", oneline_string)
mo2 = re.match("Vien", oneline_string)
print(mo1)
print(mo1.group('name'))
print(mo2)
del mo1, mo2

mo1 = re.search("Hello", oneline_string)
mo2 = re.match("Hello", oneline_string)
print(mo1)
print(mo2)
del mo1, mo2

mo1 = re.search("Vien", oneline_string)
mo2 = re.search("Vien", multiline_string, re.M)
mo3 = re.findall("Vien", multiline_string)
print(mo1)
print(mo2)
print(mo3)

for mo4 in re.finditer("Vien", multiline_string):
    print(mo4)
    print(mo4.group())
    print(mo4.span())
del mo1, mo2, mo3, mo4

print("Hello Vien\nBye Vien")
print(r"Hello Vien\nBye Vien") #raw string doesn't process backslash as escape character

print(re.sub("Vien", "Van", multiline_string))

print(re.split("Vien", multiline_string))

mo = re.match("Hello (?P<name>\w+)\n.*\n.*(?P=name)",multiline_string)
print(mo)
print(mo.groups())
print(mo.group('name'))

phonebook = """\
Vien Mai, 12345
Van Dw, 56789 
"""
for line in phonebook.splitlines():
    mo = re.match("(?P<fname>\w+)\s(?P<lname>\w+),\s(?P<number>\d+)", line)
    print(mo)
    print(mo.groups())
    print(mo.group('fname'))
    print(mo.group('lname'))
    print(mo.group('number'))

mix_string = "abc 123 r 56 x 78"
print(re.findall("\d+",mix_string))
mo = re.match("(\w+\s\d+\s?)+",mix_string)
print(mo.groups())
print(mo)
print(mo.group(0))
print(mo.group(1))
for grp in mo.groups():
    print(grp)