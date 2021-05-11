#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    print(pet, end = " ")

print()

for i in range(10):
    print(i, end = " ")

print()

for i in range(10):
    print(i, end = " ")
    if i == 5:
        break
else:
    print("exited normally")

print()

for i in range(10):
    print(i, end = " ")
else:
    print("exited normally")



