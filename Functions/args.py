#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')
    my_print(1, 2, 3, 4)
    my_print()


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')


def my_print(*args):
    if len(args):
        for s in args:
            print(s, end=' ')
    else:
        print("There is no input")
    print()

if __name__ == '__main__': main()
