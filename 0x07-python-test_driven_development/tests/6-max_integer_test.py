#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest class for testing max_integer function
    """
    def test_max(self):
        """testing with different values"""
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)
        self.assertEqual(max_integer([5, 2, 3, 5]), 5)
        self.assertEqual(max_integer([1, 1, 1, -4]), 1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([5, 6, 5, 5]), 6)
        self.assertEqual(max_integer(["1", "2", "4"]), "4")

    def test_values(self):
        """testing with non numeric values"""
        self.assertRaises(TypeError, max_integer, [1, "5", 4])
        self.assertRaises(TypeError, max_integer, [1, "fady", 4])
        self.assertRaises(TypeError, max_integer, [[1, 4, 6], "fady", 4])
        self.assertRaises(TypeError, max_integer, [[1, 4, 6], 2, 4])
        self.assertRaises(TypeError, max_integer, None)

    def test_empty(self):
        """testing empty arguments"""
        self.assertIsNone(max_integer())
