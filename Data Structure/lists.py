#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # List- mutable
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(", ".join(game))
    print(len(game))
    print_list(game)
    print(game[1:3])
    print(game[1:5:2])
    print(game.index("Paper"))
    print(game[1])
    game.append("Laptop")
    print_list(game)
    game.insert(0, "Computer")
    print_list(game)
    game.remove("Computer")
    print_list(game)
    x = game.pop()
    print(x)
    print_list(game)
    x = game.pop(2)
    print(x)
    print_list(game)
    del game[1]
    print_list(game)
    del game[1:3]
    print_list(game)

    # Tuple- immutable
    game_tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # game_tuple.append("Computer")


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == '__main__': main()
