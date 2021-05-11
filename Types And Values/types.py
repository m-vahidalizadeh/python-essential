#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

x = "7"
y = 7
z = 7.1
a = 'seven'
b = "seven"
c = '''
My first name is Mohammad.
My last name is Vahidalizadeh.
I got my Ph.D. in Computer Science.
'''
d = """
My first name is Mohammad.
My last name is Vahidalizadeh.
I got my Ph.D. in Computer Science.
"""
e = "seven".upper()
f = 7 * 3
g = 7 * 3.14159
h = 7 / 3
i = 7 // 3
j = 7 % 3
k = .1 + .1 + .1 - .3
l = Decimal(".1")
m = Decimal(".3")
n = l + l + l - m
o = True
p = 7 > 5
q = False
r = None
s = ""
t = "t"
t2 = 1
t3 = 0

print('x is {}'.format(x))
print(type(x))
print(type(y))
print(f'The type of z is {type(z)}')
print(f'Type of {a} is {type(a)}')
print(f'Type of {b} is {type(b)}')
print(f'Type of {c} is {type(c)}')
print(f'Type of {d} is {type(d)}')
print(f"seven in capital letters is {e}")
print(f"6 {y:<9} 8")
print(f"6 {y:>9} 8")
print(f"6 {y:<09} 8")
print(f"6 {y:>09} 8")
print(f"f is {f} and it's type is {type(f)}")
print(f"f is {g} and it's type is {type(g)}")
print(f"f is {h} and it's type is {type(h)}")
print(f"f is {i} and it's type is {type(i)}")
print(f"f is {j} and it's type is {type(j)}")
print(f"f is {k} and it's type is {type(k)}")
print(f"f is {n} and it's type is {type(n)}")
print(f"f is {o} and it's type is {type(o)}")
print(f"f is {p} and it's type is {type(p)}")
print(f"f is {q} and it's type is {type(q)}")
print(f"f is {r} and it's type is {type(r)}")
print(f"r {r}")
if r:
    print("True")
else:
    print("False")
print(f"s {s}")
if s:
    print("True")
else:
    print("False")
print(f"t {t}")
if t:
    print("True")
else:
    print("False")
print(f"t2 {t2}")
if t2:
    print("True")
else:
    print("False")
print(f"t3 {t3}")
if t3:
    print("True")
else:
    print("False")

t4 = (1, "two", 3.0, [4, "four"], 5)
t5 = (1, "two", 3.0, [4, "four"], 5)
t6 = [1, "two", 3.0, [4, "four"], 5]
print(f't4 is {t4}')
print(f't4 type is {type(t4)}')
print(f"t4[3] type is {type(t4[3])}")
print(f"t4 id is {id(t4)}")
print(f"t5 id is {id(t5)}")
print(f"t4[0] id is {id(t4[0])}")
print(f"t5[0] id is {id(t5[0])}")
if t4[0] is t5[0]:
    print("Yes")
else:
    print("No")
if t4 is t5:
    print("Yes")
else:
    print("No")
if isinstance(t4, tuple):
    print(f"t4 is a tuple")
elif isinstance(t4, list):
    print(f"t4 is a list")
if isinstance(t6, tuple):
    print(f"t6 is a tuple")
elif isinstance(t6, list):
    print(f"t6 is a list")
