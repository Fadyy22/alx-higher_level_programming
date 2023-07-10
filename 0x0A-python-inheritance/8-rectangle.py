#!/usr/bin/python3

"""module containing 'BaseGeometry' Class and 'Rectangle' Class"""


class BaseGeometry:
    """class 'BaseGeometry'"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """'Rectangle' class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__wdith = width
        self.__height = height
