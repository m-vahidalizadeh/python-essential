#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# mutable
x = [1, 2, 3, 4, 5]
x[2] = 42
# Immutable
# x2 = (1, 2, 3, 4, 5)
# x2[2] = 42
# Immutable
x3 = range(5)
x4 = range(5, 10)
x5 = range(5, 11, 5)
# Mutable
x6 = list(range(10))
x6[2] = 42
for i in x:
    print('i is {}'.format(i))
for i in x3:
    print(f"i is {i}")
for i in x4:
    print(f"i is {i}")
for i in x5:
    print(f"i is {i}")
for i in x6:
    print(f"i is {i}")
# Dictionary- mutable
x7 = {"One": 1, "Two": 2, "Three": 3}
x7["Three"] = 42
for i in x7:
    print(f"i is {i}")
for k, v in x7.items():
    print(f" k:{k} v:{v}")
