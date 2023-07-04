#!/usr/bin/python3
"""

a module containing an add_integer function

"""


from audioop import add


def add_integer(a, b=98):
    """a function that adds integers and/or floats

    Args:
        a (int): the first number to be added
        b (int): the second number to be added

    Returns:
        int: the sum of 'a' and 'b'

    Raises:
        TypeError: if the type of 'a' or 'b' is not integer/float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
