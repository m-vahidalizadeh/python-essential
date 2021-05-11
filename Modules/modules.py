#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(f"Platform: {sys.platform}")
    print(os.name)
    print(os.getenv("PATH"))
    print(os.getcwd())
    print(os.urandom(25).hex())
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    x = datetime.datetime.now()
    print(x)
    print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)


if __name__ == '__main__': main()
