#!/usr/bin/python3
import hidden_4 as h


def r():
    for i in dir(h):
        if i[0] != '_':
            print(i)


if __name__ == '__main__':
    r()
