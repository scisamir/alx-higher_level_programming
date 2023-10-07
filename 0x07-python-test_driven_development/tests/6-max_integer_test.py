#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test max_integer """

    def test_correct_input(self):
        """ Test with the right input """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """ Test for empty_list """
        self.assertEqual(max_integer([]), None)
