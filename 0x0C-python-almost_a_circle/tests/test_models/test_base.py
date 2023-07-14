#!/usr/bin/python3

"""test module for base class"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """BaseTest class for testing base class"""

    def setUp(self):
        Base.set_nb_objects(0)

    def test_input_id(self):
        new = Base(16)
        self.assertEqual(new.id, 16)

    def test_nb_objects_id(self):
        new1 = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_combined_id(self):
        new1 = Base()
        new2 = Base(51)
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 51)
        self.assertEqual(new3.id, 2)
