#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:

    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Animal2:

    def __init__(self, **kwargs):
        self._type = kwargs["type"] if "type" in kwargs else "Plane"
        self._name = kwargs["name"] if "name" in kwargs else "Jimbo"
        self._sound = kwargs["sound"] if "sound" in kwargs else "vow!"

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def print_animal2(o):
    if not isinstance(o, Animal2):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))
    a2 = Animal2(type="Elephant", name="Dumbo", sound="Lil!")
    print_animal2(a2)
    print_animal2(Animal2())


if __name__ == '__main__': main()
