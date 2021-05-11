#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class MyString(str):
    def __str__(self):
        return self[::-1]


print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.swapcase())
print('Hello, World.'.title())
print('Hello, World. {}'.format(42 * 7))
print("""
Hello, 
World.
{}
""".format(42 * 7))
s = "Hello, world! {}"
print(s.format(42 * 7))
s = MyString("Hello, world!")
print(s)
# Concat
a = "Mohammad"
b = "Vahidalizadeh"
print(a + " " + b)
x = 42
y = 73
print("The numbers are {bb} {xx}.".format(xx=x, bb=y))
print("The numbers are {1} {0}.".format(x, y))
print("The numbers are {0} {1} {0}.".format(x, y))
print("The numbers are {0:>05} {1:+05} {0:<7}.".format(x, y))
x = x * 747 * 1000
print("The number is {:,}".format(x))
print("The number is {:,}".format(x).replace(",", "."))
print("The number is {:f}".format(x))
print("The number is {:.3f}".format(x))
x = 42
print(f"The number is {x:b}")


