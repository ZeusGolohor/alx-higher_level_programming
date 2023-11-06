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

