#!/usr/bin/python3
"""

a module containing a say_my_name function

"""


def say_my_name(first_name, last_name=""):
    """a function that prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
