#!/usr/bin/python3
"""
This module is an empty BaseGeometry class.
"""
Rectangle = __import__("9-rectangle").Rectangle
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
