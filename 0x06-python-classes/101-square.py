#!/usr/bin/python3

"""This class represents a square class"""


class Square:
    """Square class that defines a square and
    initializes a value for its size
    """

    def __str__(self):
        rtr = ""
        if self.__size == 0:
            rtr += "\n"
        else:
            for i in range(self.position[1]):
                rtr += "\n"
            for k in range(self.__size):
                for j in range(self.position[0]):
                    rtr += " "
                for o in range(self.__size):
                    rtr += "#"
                rtr += "\n"
        return rtr

    def __init__(self, size=0, position=(0, 0)):
        """init the square with a private attribute (size)"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter function"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter function"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter function"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area function returns the area of the square
        area = size * size"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square using '#' sign"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for k in range(self.__size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for o in range(self.__size):
                    print("#", end="")
                print()
