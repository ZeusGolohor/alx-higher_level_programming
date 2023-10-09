#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_a = ()
    new_b = ()
    if (len(tuple_a) >= 2):
        new_a = (tuple_a[0], tuple_a[1])
    elif (len(tuple_a) == 1):
        new_a = (tuple_a[0], 0)
    elif (len(tuple_a) == 0):
        new_a = (0, 0)

    if (len(tuple_b) >= 2):
        new_b = (tuple_b[0], tuple_b[1])
    elif (len(tuple_b) == 1):
        new_b = (tuple_b[0], 0)
    elif (len(tuple_b) == 0):
        new_b = (0, 0)

    return (new_a[0] + new_b[0], new_a[1] + new_b[1])
