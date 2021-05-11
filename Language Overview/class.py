#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')


class Person:
    name = 'default'
    sur_name = 'default'

    def __init__(self, name, sur_name):
        self.name = name
        self.sur_name = sur_name

    def tell_name(self):
        print(f'My name is {self.name}.')

    def tell_family_name(self):
        print(f'My family name is {self.sur_name}')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    mohammad = Person('Mohammad', 'Alizadeh')
    mohammad.tell_name()
    mohammad.tell_family_name()


if __name__ == '__main__': main()
