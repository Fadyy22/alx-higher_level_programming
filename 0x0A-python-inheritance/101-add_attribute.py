#!/usr/bin/python3

"""module containing 'add_attribute' function"""


def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it is possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
