#!/usr/bin/python3
"""
This module is used for unittest.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        """
        unittest to check if none is returned
        for an empty function call
        """
        self.assertEqual(max_integer([]), None)

    def test_max_at_end(self):
        """
        unittest for max at the end.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """
        unittest for max at the beginning
        """
        self.assertEqual(max_integer([12, 2, 3, 4]), 12)

    def test_for_max_middle(self):
        """
        unittest for max at the middle
        """
        self.assertEqual(max_integer([12, 2, 13, 3, 4]), 13)

    def test_for_negative_number(self):
        """
        unittest for negative
        """
        self.assertEqual(max_integer([-2, 13]), 13)

    def test_for_one_element(self):
        """
        unnitest for one element
        """
        self.assertEqual(max_integer([13]), 13)

    def test_for_only_negative_numbers(self):
        """
        unittest for only negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)
