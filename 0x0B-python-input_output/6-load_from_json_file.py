#!/usr/bin/python3
"""
This module is used to create an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    This method is used to create an Object from a JSON
    file.
    """
    json_str = ""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        json_str = "".join(a_file.read())

    return (json.loads(json_str))
