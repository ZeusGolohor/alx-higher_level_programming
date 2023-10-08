#!/usr/bin/pthon3


def print_reversed_list_integer(my_list=[]):
    i = (len(my_list) - 1)
    if my_list is not None:
        for x in my_list:
            print('{:d}'.format(my_list[i]))
            i = i - 1
