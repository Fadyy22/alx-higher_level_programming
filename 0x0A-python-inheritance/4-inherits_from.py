#!/usr/bin/python3

"""module containing 'inherits_from' function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False

    Args:
        obj: object to check
        a_class: the class to check if 'obj' is an instance of a class that
        inherited (directly or indirectly) from the specified class

    Return:
        True: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        False: otherwise
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
