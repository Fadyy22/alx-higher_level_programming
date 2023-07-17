#!/usr/bin/python3

"""test module for rectangle class"""

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """RectangleTest class for testing rectangle class"""

    def setUp(self):
        Base.set_nb_objects(0)
        self.output = StringIO()
        sys.stdout = self.output

    def test_width_height_x_y_non_int(self):
        """tests width height x y not int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1.5, 15)
        with self.assertRaises(TypeError):
            rec = Rectangle(15, 1.5)
        with self.assertRaises(TypeError):
            rec1 = Rectangle(15, 15, 1.3, 2)  # type: ignore
        with self.assertRaises(TypeError):
            rec1 = Rectangle(15, 15, 1, 2.1)  # type: ignore

    def test_width_height_less_than_or_equal_zero(self):
        """tests width height <= 0"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-5, 10)
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -10)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 0)

    def test_x_y_less_than_zero(self):
        """tests x y < 0"""
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 10, -5, 2)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 10, 2, -4)

    def test_area(self):
        """tests area function"""
        rec = Rectangle(10, 15)
        self.assertEqual(rec.area(), 150)

    def test_str_(self):
        """tests __str__"""
        rec = Rectangle(10, 15, 7, 6)
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 7/6 - 10/15")

    def test_display(self):
        """tests dispaly function with only width and height"""
        rec = Rectangle(2, 4)
        rec.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n##\n##\n")

    def test_display_with_x(self):
        """tests dispaly function with only width and height and x"""
        rec = Rectangle(2, 4, 2, 0)
        rec.display()
        self.assertEqual(self.output.getvalue(), "  ##\n  ##\n  ##\n  ##\n")

    def test_display_with_x_and_y(self):
        """tests dispaly function with only width and height and x and y"""
        rec = Rectangle(2, 4, 2, 1)
        rec.display()
        self.assertEqual(self.output.getvalue(), "\n  ##\n  ##\n  ##\n  ##\n")

    def test_args_update(self):
        """tests update function with args"""
        rec = Rectangle(10, 10, 10, 10)
        rec.update(89, 15, 20, 13, 11)
        print(rec)
        msg = "[Rectangle] (89) 13/11 - 15/20\n"
        self.assertEqual(self.output.getvalue(), msg)

    def test_kwargs_update(self):
        """tests udpate function with kwargs"""
        rec = Rectangle(10, 10, 10, 10)
        rec.update(id=13, x=15, y=12, width=5, height=8)
        print(rec)
        msg = "[Rectangle] (13) 15/12 - 5/8\n"
        self.assertEqual(self.output.getvalue(), msg)

    def test_to_dictionary(self):
        """tests to_dictionary function"""
        rec = Rectangle(10, 2, 1, 9)
        rec_dictionary = rec.to_dictionary()
        my_dect = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(rec_dictionary, my_dect)

    def test_to_json_string(self):
        """test to_json_string function"""
        rec = Rectangle(10, 2, 1, 9)
        rec_dictionary = rec.to_dictionary()
        rec_list = Rectangle.to_json_string([rec_dictionary])
        json_string = '[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}]'
        self.assertEqual(rec_list, json_string)

    def test_to_json_string_none(self):
        """tests to_json_string using None"""
        rec_list = Rectangle.to_json_string(None)
        print(rec_list)
        json_string = "[]\n"
        self.assertEqual(self.output.getvalue(), json_string)

    def test_from_json_string(self):
        """tests from_json_string function"""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        result = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(list_output, result)

    def test_from_json_string_none(self):
        """tests from_json_string using None"""
        list_output = Rectangle.from_json_string(None)
        result = []
        self.assertEqual(list_output, result)
