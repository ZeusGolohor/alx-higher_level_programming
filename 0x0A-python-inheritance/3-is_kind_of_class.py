#!/usr/bin/python3
"""
This module is used to check if an object is a subclass of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    This module is used to check if an object is a subclass of a class.
    """
    if (issubclass(type(obj), a_class) is True):
        return (True)
    return (False)
