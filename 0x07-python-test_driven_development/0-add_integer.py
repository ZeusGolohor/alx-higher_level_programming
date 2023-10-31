#!/usr/bin/python3
"""
    This module is for the calculation of two numbers.
"""
import math


def add_integer(a, b=98):
    """
    This function is used for the calculation of two numbers.
    """
    if ((isinstance(a, int) is True or isinstance(a, float) is True)
            and (isinstance(b, int) is True or isinstance(b, float) is True)):
        if (a is NaN):
            raise TypeError('a must be an integer')
        elif (math.isnan(b) is True):
            raise TypeError('b must be an integer')

        a = int(a)
        b = int(b)
        return ((a + b))
    else:
        if (a is None or b is None):
            raise TypeError('a must be an integer')
        elif ((isinstance(a, str) is True or isinstance(a, int) is False)
                and isinstance(a, float) is False):
            raise TypeError('a must be an integer')
        elif (isinstance(b, int) is False or isinstance(b, float) is False):
            raise TypeError('b must be an integer')
