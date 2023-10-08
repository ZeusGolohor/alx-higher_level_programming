#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    if (my_string is not None):
        for char in my_string:
            if (char not in "cC"):
                new_string = new_string + char
        return (new_string)
