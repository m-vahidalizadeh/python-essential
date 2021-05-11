#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

name = 'Mohammad'
def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('My name is {}'.format(name))
    if False: # This is a comment
        print('true')
    else:
        print('Not in true')


if __name__ == '__main__': main()
