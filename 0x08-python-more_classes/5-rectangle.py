#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """an empty class Rectangle that defines a rectangle"""

    def __str__(self):
        rtn = ""
        if self.__height == 0 or self.__width == 0:
            return rtn
        for i in range(self.__height):
            for j in range(self.__width):
                rtn += "#"
            if i != self.__height - 1:
                rtn += "\n"
        return rtn

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print(f"Bye rectangle...")

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter to retrieve the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter to retrieve the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
