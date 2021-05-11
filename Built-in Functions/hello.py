#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f"repr: the number of bunnies is {self._n}🖖"

    def __str__(self):
        return f"str: the number of bunnies is {self._n}"


print('Hello, World.')
s = "Hello, world."
print(repr(s))
s = Bunny(47)
print(repr(s))
print(s)
print(ascii(s))
print(chr(128406))
print(ord("🖖"))


def print_list(l):
    for i in l:
        print(i, end=" ")
    print()


x = (1, 2, 3, 4, 5)
y = x
print_list(x)
print_list(y)
y = len(x)
print(y)
y = reversed(x)
print_list(y)
y = list(reversed(x))
print_list(y)
y = sum(x)
print(y)
y = sum(x, 10)
print(y)
y = max(x)
print(y)
y = min(x)
print(y)
print(any(x))
y = (0, 1, 0, 0, 0)
print(any(y))
print(all(y))
y = (6, 7, 8, 9, 10)
z = zip(x, y)
for a, b in z:
    print(f"{a} - {b}, ", end=" ")
print()
y = ("cat", "dog", "rabbit")
for i, v in enumerate(x):
    print(f"{i}: {v}", end=", ")
print()

x = 42
y = type(x)
print(x)
print(y)
print(isinstance(x, int))
print(id(x))
