#!/usr/bin/python3

"""module containing 'Rectangle' Class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """'Rectangle' class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__wdith = width
        self.__height = height
