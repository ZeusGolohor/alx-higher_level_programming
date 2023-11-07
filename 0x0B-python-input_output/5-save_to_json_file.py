#!/usr/bin/python3
"""
This module is used to write an Object to
a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This method is used to write an Object to
    a text file, using JSON representation.
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))
