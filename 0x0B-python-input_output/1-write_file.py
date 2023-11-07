#!/usr/bin/python3
"""
This module is used to write a string
to a text file.
"""


def write_file(filename="", text=""):
    """
    This method is used to write a string
    to a text file.
    """
    total_len = 0
    with open(filename, mode="w", encoding="utf-8") as a_file:
        for string in text:
            total_len = total_len + 1
        a_file.write(text)

    return (total_len)
