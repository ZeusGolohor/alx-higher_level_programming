#!/usr/bin/python3
"""
This module is a subclass of the base geometry class.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
