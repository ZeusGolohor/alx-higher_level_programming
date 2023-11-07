#!/usr/bin/python3
"""
This module is return the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    This method is used to return the dictionary description
    with simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    new_dic = {}
    for word in dir(obj):
        if ((word[0] != "_") and (word[1] != "_")):
            if (isinstance(getattr(obj, word),
               (list, dict, str, int, bool)) is True):
                new_dic[word] = getattr(obj, word)
        elif ((word[-1] != "_") and (word[-2] != "_")):
            new_dic[word] = getattr(obj, word)

    return (new_dic)
