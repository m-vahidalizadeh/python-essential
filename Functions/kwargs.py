#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    x = dict(Mohammad= "Alizadeh", Ali= "Alizadeh", Mahnaz= "Heidarzadeh")
    print_dict(**x)

def print_dict(**kwargs):
    for k in kwargs:
        print(f"key {k} value {kwargs[k]}")

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
