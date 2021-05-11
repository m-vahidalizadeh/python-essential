#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
z = float(x)
print(f"z {z} type is {type(z)}")
x = -47
z = abs(x)
print(f"abs of {x} is {z}")
x = 47
y = divmod(x, 3)
print(y)
y = x + 73j
print(f'y {y} is {type(y)}')
y = complex(x, 73)
print(f'y {y} is {type(y)}')

