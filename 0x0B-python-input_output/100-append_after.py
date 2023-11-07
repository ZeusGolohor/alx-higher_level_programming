#!/usr/bin/python3
"""
This module is used to insert a line of
text to a file, after each line containing
a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This method is used to inserts a line
    of text to a file, after each line containing
    a specific string.
    """
    new_word_list = []
    with open(filename, mode="r", encoding="utf-8") as a_file:
        for a_line in a_file:
            if (search_string in a_line):
                new_word_list.append(a_line)
                new_word_list.append(new_string)
            else:
                new_word_list.append(a_line)

    with open(filename, mode="w", encoding="utf-8") as a_file:
        for a_string in new_word_list:
            a_file.write(a_string)
