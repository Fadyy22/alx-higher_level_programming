#!/usr/bin/python3
"""

a module containing a print_square function

"""


def print_square(size):
    """a function that prints a square with the character #

    Args:
        size: the size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
