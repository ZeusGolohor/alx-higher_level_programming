#!/usr/bin/python3
"""
This module is used to check if the object is an instance of
a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    This module is used to check if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class.
    """
    return (not(type(obj) is a_class) and isinstance(obj, a_class))
