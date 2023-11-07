#!/usr/bin/python3
"""
This module is used to convert a class to json.
"""


class Student:
    """
    This class contains the student
    information
    """
    def __init__(self, first_name, last_name, age):
        """
        This method called once this class is used
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrieves a dictionary
        representation of a class.
        """
        obj = self
        new_dic = {}
        for word in dir(obj):
            if ((word[0] != "_") and (word[1] != "_")):
                if (isinstance(getattr(obj, word),
                   (list, dict, str, int, bool)) is True):
                    if (attrs is None):
                        new_dic[word] = getattr(obj, word)
                    else:
                        for attr in attrs:
                            if (attr is word):
                                new_dic[word] = getattr(obj, word)
            elif ((word[-1] != "_") and (word[-2] != "_")):
                if (attrs is None):
                    new_dic[word] = getattr(obj, word)
                else:
                    for attr in attrs:
                        if (attr == word):
                            new_dic[word] = getattr(obj, word)

        return (new_dic)
