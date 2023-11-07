#!/usr/bin/python3
"""
This module is used to read a file in UTF8 mode.
"""


def read_file(filename=""):
    """
    This method reads a file and prints it's content
    to the standard output.
    """
    with open(filename, 'r', encoding="utf-8") as a_file:
        for a_line in a_file:
            print(a_line, end="")
