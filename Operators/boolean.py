#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
z = "deer"

if a and b:
    print('expression is true')
else:
    print('expression is false')

if y in x:
    print(f"{y} is in {x}")

if z not in x:
    print(f"{z} not in {x}")

if y is x[0]:
    print(f"{y} (id={id(y)}) is the first element of {x} (id={id(x[0])})")




