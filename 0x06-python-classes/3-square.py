#!/usr/bin/python3

"""This class represents a square class"""


class Square:
    """Square class that defines a square and
    initializes a value for its size
    """

    def __init__(self, size=0):
        """init the square with a private attribute (size)"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area function returns the area of the square
        area = size * size"""
        return self.__size * self.__size
