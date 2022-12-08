#!/usr/bin/python3
import sys


def r():
    n = 0
    if (len(sys.argv) == 1):
        print('{:d}'.format(n))
    else:
        for i in range(1, len(sys.argv)):
            n += int(sys.argv[i])

        print('{}'.format(n))


if __name__ == '__main__':
    r()
