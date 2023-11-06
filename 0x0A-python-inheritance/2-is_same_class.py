#!/usr/bin/python3
"""
This module is used to check if a value is an instance of
a specific class.
"""


def is_same_class(obj, a_class):
    """
    This module is used to check if a value is an instance of
    a specific class.
    """
    if (a_class == object or obj is None):
        return (False)

    if (isinstance(obj, a_class) is True):
        if ((isinstance(obj, int) is True) and
                (isinstance(obj, bool) is True)):
            return (False)
        return (True)
    else:
        return (False)
