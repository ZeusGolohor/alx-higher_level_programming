#!/usr/bin/python3
"""
This module is used to  prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This module is used to  prints a text with 2 new
    lines after each of these characters: ., ? and :
    """
    if (isinstance(text, str) is False):
        raise TypeError('text must be a string')
    position = 0
    print(text[position], end='')
    for i in range(len(text)):
        position = i
        if (text[position] == '.'
                or text[position] == '?' or text[position] == ':'):
            print()
            print()
        else:
            position = position + 1
            if (position < len(text)):
                print(text[position], end='')
