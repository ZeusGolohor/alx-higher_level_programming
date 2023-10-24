#!/usr/bin/python3
"""
The Square class is an empty class that is used
to demonstrate how classes works
"""


class Square:
    """
    The Square class is an empty class that is used
    to demonstrate how classes works
    """
    def __init__(self, size=0):
        self.__size_att = size

    @property
    def __size_att(self):
        return (self.__size)

    @__size_att.setter
    def __size_att(self, x):
        if isinstance(x, int) is False:
            raise TypeError("size must be an integer")
        else:
            if x < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = x

    def area(self):
        return (self.__size * self.__size)
