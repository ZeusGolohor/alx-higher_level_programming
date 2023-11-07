#!/usr/bin/python3
"""
This module returns the JSON representation
of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    This method returns the JSON representation
    of an object (string).
    """
    return (json.dumps(my_obj))
