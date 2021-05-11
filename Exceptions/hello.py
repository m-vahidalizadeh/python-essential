#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys


def main():
    print('Hello, World.')
    try:
        x = int("Mohamamd")
    except ValueError:
        print("I caught a value error!")

    try:
        y = 5 / 0
    except ZeroDivisionError:
        print("don\'t divide by zero.")
    else:
        print("good job!")

    try:
        y = 5 / 2
    except ZeroDivisionError:
        print("don\'t divide by zero.")
    else:
        print("good job!")

    try:
        y = 5 / 0
    except:
        print(f"Unknown error: {sys.exc_info()}")
    else:
        print("good job!")


if __name__ == '__main__': main()
