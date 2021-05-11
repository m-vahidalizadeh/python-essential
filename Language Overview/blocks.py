#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 2
y = 2
z = 112

if x < y:
    print(f'{x} < {y}')
    # print('x < y: x is {} and y is {}'.format(x, y))
    # print(f'x < y: x is {x} and y is {y}')
elif x > y:
    print(f'{x} > {y}')
else:
    print(f'{x} = {y}')

print(f'something else {z}')

