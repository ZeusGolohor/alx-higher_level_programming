#!/usr/bin/python3
"""
This module is used to print a formated string
"""


def say_my_name(first_name, last_name=""):
    """
    This function is used to print a formated string
    """
    if (isinstance(first_name, str) is False):
        raise TypeError('first_name must be a string')
    if (isinstance(last_name, str) is False):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
