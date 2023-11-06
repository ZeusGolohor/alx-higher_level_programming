#!/usr/bin/python3
"""
This module is an empty BaseGeometry class.
"""


class BaseGeometry:
    """
    This module is an empty BaseGeometry class.
    """
    def area(self):
        """
        This is used to raise an expection meassage.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method is used to validate value.
        """
        if ((isinstance(value, int)) is False or
                isinstance(value, bool) is True):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This is a subclass that inherits from BaseGeometry class.
    """
    def __init__(self, width, height):
        """
        Rectangle class instanciation function.
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """
        This is used to raise an expection meassage.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        The string to be return by the print function.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    This is a grandChild class of BaseGeometry
    """
    def __init__(self, size):
        """
        Square class constructor.
        """
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """
        Used to calculate the area of a square.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        The string to be returned by the print function.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
