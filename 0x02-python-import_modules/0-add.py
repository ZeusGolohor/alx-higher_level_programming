#!/usr/bin/python3
from add_0 import add


def res():

    a = 1
    b = 2
    c = add(a, b)
    print('{} + {} = {}'.format(a, b, add(a, b)))


if __name__ == "__main__":
    res()

