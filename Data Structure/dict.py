#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    animals2 = dict(kitten='meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr')
    print("animals:")
    print_dict(animals)
    print("animals2:")
    print_dict(animals2)
    print_dict2(animals)
    print_dict_keys(animals)
    print_dict_values(animals)
    animals["lion"] = "I am a lion!"
    print(animals["lion"])
    animals["Monkey"] = "I am a monkey!"
    print_dict(animals)
    print("lion" in animals)
    print("pig" in animals)
    print("Found!" if "lion" in animals else "Nope!")
    print(animals.get("lion"))


def print_dict_keys(d):
    for k in d.keys():
        print(f"key: {k}", end=" ")
    print()


def print_dict_values(d):
    for v in d.values():
        print(f"value: {v}", end=" ")
    print()


def print_dict(o):
    for x in o: print(f'{x}: {o[x]}', end=" ")
    print()


def print_dict2(d):
    for k, v in d.items():
        print(f"{k}-> {v}", end=" ")
    print()


if __name__ == '__main__': main()
