#!/usr/bin/python3

"""module containing 'is_same_class' function"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    ; otherwise False

    Args:
        obj: object to check
        a_class: the class to check if 'obj' is an instance from

    Return:
        True: if if the object is exactly an instance of the specified class
        False: otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
