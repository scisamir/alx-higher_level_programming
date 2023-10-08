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

    def test_max_at_beginning(self):
        """ Test for max at beginning """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_negative(self):
        """ Test for one negative number in the list """
        self.assertEqual(max_integer([-4, 1, 2, 3]), 3)

    def test_all_negative(self):
        """ Test for only negative numbers in the list """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_one_element(self):
        """ Test for list of one element """
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """ Test for empty_list """
        self.assertEqual(max_integer([]), None)
