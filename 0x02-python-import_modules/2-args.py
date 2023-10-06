#!/usr/bin/python3
import sys


def args():
    i = len(sys.argv)
    x = 1
    print("{:d} argument".format((i - 1)))
    while (x < i):
        print("{:d} {}".format(x, sys.argv[x]))
        x = x + 1


if __name__ == "__main__":
    args()
