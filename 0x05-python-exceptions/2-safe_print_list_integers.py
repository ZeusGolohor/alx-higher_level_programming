#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for i in range(x):
            if (isinstance(my_list[i], int) is True):
                total += 1
                print('{:d}'.format(my_list[i]), end='')
        print()
    except Exception:
        raise
    return (total)
