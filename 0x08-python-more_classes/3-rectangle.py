#!/usr/bin/python3
"""
This module is a simple Rectangle module.
"""


class Rectangle:
    """
    This is a simple rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if ((self.width == 0) or (self.height == 0)):
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """
        Used to return a nicely printed user friendly
        string.
        """
        string = ''
        if (self.__height == 0):
            return (string)
        if (self.__width == 0):
            return (string)

        for i in range(self.__height):
            for x in range(self.__width):
                string = string + '#'
            string = string + '\n'
        return (string)
