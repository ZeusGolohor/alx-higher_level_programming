#!/usr/bin/python3
import sys


def r():
    if len(sys.argv) == 1:
        print('{} arguments.'.format(0))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print('{}: {}'.format(i, sys.argv[i]))


if __name__ == '__main__':
    r()
