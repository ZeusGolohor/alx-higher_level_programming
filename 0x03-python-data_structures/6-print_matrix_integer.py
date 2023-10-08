#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, x in enumerate(i):
            print("{:d}".format(x), end="")
            if (idx < (len(i) - 1)):
                print("{}".format(" "), end="")
        print()
