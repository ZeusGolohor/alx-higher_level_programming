#!/usr/bin/python3
"""
This model is used to test rectangle model
using unittest.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    This class is used to test the
    Rectangle model.
    """
    def test_rectangle_isinstance(self):
        """
        Used to test that an object is an instance
        of the Rectangle class.
        """
        self.assertIsInstance(Rectangle(1, 2), Base)

if __name__ == "__main__":
    unittest.main()
