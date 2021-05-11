#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    print("this is f1")


def f2():
    def f3():
        print("this is f3")
    return f3

print('Hello, World.')
x = f1
x()
x = f2()
x()

