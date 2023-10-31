#!/usr/bin/python3
"""
This module is used to print a square with the character #.
"""


def print_square(size):
    """
    This function is used to print a square with the character #.
    """
    if (isinstance(size, int) is False):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    if ((isinstance(size, float) is True) and (size < 0)):
        raise TypeError('size must be an integer')
    for i in range(size):
        for x in range(size):
            print('#', end='')
        print()
