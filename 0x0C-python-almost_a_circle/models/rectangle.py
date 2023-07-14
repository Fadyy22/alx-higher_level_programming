#!/usr/bin/python3

"""module containing rectangle class that inherits from Base class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """width getter and setter"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """height getter and setter"""

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """x getter and setter"""

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """y getter and setter"""

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()
