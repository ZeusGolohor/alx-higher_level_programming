#!/usr/bin/python3
import sys


def add():
    res = 0
    for i in range(1, len(sys.argv)):
        res = res + int(sys.argv[i])
    print("{:d}".format(res))


if __name__ == "__main__":
    add()
