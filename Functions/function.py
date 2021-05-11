#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(5)
    x = kitten()
    print(x)
    print(f"x {x} x type {type(x)}")
    x = kitten2()
    print(x)
    print(f"x {x} x type {type(x)}")
    y = kitten2()
    print(y)
    my_print(1, 2, 3)
    my_print(1, 2)
    my_print(1)
    x = 5
    x2 = x
    my_print2(x)
    print(f"x is {x}")
    print(id(x))


def kitten(n=2):
    print(f'{n} Meow.')


def kitten2(n=2):
    return f'{n} Meow.'


def my_print(a, b=1, c=0):
    print(a, b, c)


def my_print2(a):
    print(id(a))
    a = 3
    print(id(a))
    print(a)


if __name__ == '__main__':
    main()
