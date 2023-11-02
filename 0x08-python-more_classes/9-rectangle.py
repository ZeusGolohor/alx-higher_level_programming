#!/usr/bin/python3
"""
This module is a simple Rectangle module.
"""


class Rectangle:
    """
    This is a simple rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return (self.__width * self.__height)

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
        sym = ''
        try:
            if (self.print_symbol is None):
                raise AttributeError()
            sym = self.print_symbol
        except AttributeError:
            sym = Rectangle.print_symbol

        for i in range(self.__height):
            for x in range(self.__width):
                string = string + str(sym)
            if ((i + 1) != self.__height):
                string = string + '\n'
        self.print_symbol = None
        return (string)

    def __repr__(self):
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")

        r1 = rect_1.area()
        r2 = rect_2.area()
        if (r1 == r2):
            return (rect_1)
        elif (r1 > r2):
            return (rect_1)
        elif (r1 < r2):
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance.
        """
        if (isinstance(size, int) is False):
            raise TypeError('width must be an integer\nBye rectangle...')
        new = cls(size, size)
        return (new)
