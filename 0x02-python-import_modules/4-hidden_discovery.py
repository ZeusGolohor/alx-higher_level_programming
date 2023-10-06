#!/usr/bin/python3
import hidden_4


def res():
    for name in dir(hidden_4):
        if name[1] != '_':
            print(name)


if __name__ == "__main__":
    res()
