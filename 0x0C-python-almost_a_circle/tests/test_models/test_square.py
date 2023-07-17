#!/usr/bin/python3
"""test module for square class"""

import sys
import unittest
from io import StringIO
from models.square import Square
from models.base import Base


class SquareTest(unittest.TestCase):
    """SquareTest class for testing square class"""

    def setUp(self):
        Base.set_nb_objects(0)
        self.output = StringIO()
        sys.stdout = self.output

    def test_size_non_int(self):
        with self.assertRaises(TypeError):
            sq = Square("fady")

    def test_size_less_than_or_equal_zero(self):
        with self.assertRaises(ValueError):
            sq = Square(-10)

        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_str_(self):
        sq = Square(5, 3, 4)
        self.assertEqual(sq.__str__(), "[Square] (1) 3/4 - 5")

    def test_area(self):
        sq = Square(5, 3, 5)
        self.assertEqual(sq.area(), 5 * 5)

    def test_display(self):
        sq = Square(3)
        sq.display()
        self.assertEqual(self.output.getvalue(), "###\n###\n###\n")

    def test_display_with_x(self):
        rec = Square(2, 4)
        rec.display()
        self.assertEqual(self.output.getvalue(), "    ##\n    ##\n")

    def test_display_with_x_and_y(self):
        rec = Square(2, 4, 2)
        rec.display()
        self.assertEqual(self.output.getvalue(), "\n\n    ##\n    ##\n")

    def test_args_update(self):
        rec = Square(10, 10, 10, 10)
        rec.update(89, 15, 13, 11)
        print(rec)
        msg = "[Square] (89) 13/11 - 15\n"
        self.assertEqual(self.output.getvalue(), msg)

    def test_kwargs_update(self):
        rec = Square(10, 10, 10, 10)
        rec.update(id=13, x=15, y=12, size=12)
        print(rec)
        msg = "[Square] (13) 15/12 - 12\n"
        self.assertEqual(self.output.getvalue(), msg)

    def test_to_dictionary(self):
        rec = Square(10, 2, 1)
        rec_dictionary = rec.to_dictionary()
        print(rec_dictionary)
        my_dect = "{'id': 1, 'size': 10, 'x': 2, 'y': 1}\n"
        self.assertEqual(self.output.getvalue(), my_dect)

    def test_to_json_string(self):
        """test to_json_string function"""
        rec = Square(10, 2, 1)
        rec_dictionary = rec.to_dictionary()
        rec_list = Square.to_json_string([rec_dictionary])
        json_string = '[{"id": 1, "size": 10, "x": 2, "y": 1}]'
        self.assertEqual(rec_list, json_string)

    def test_to_json_string_none(self):
        """tests to_json_string using None"""
        rec_list = Square.to_json_string(None)
        print(rec_list)
        json_string = "[]\n"
        self.assertEqual(self.output.getvalue(), json_string)

    def test_from_json_string(self):
        """tests from_json_string function"""
        list_input = [{"id": 89, "size": 10}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        result = [{"id": 89, "size": 10}]
        self.assertEqual(list_output, result)

    def test_from_json_string_none(self):
        """tests from_json_string using None"""
        list_output = Square.from_json_string(None)
        result = []
        self.assertEqual(list_output, result)
