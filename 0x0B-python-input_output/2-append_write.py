#!/usr/bin/python3
"""
This is module is used to append a string at
the end of a text file.
"""


def append_write(filename="", text=""):
    """
    This method appends a string at the
    end of a string.
    """
    total_len = 0
    with open(filename, mode="a", encoding="utf-8") as a_file:
        for char in range(len(text)):
            total_len = total_len + 1
        a_file.write(text)
    return (total_len)
