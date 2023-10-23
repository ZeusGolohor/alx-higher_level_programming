#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            total += 1
        print()
    except Exception:
        print()
    return (total)
