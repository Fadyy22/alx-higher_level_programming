#!/usr/bin/python3

"""module containing 'is_kind_of_class' function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj: object to check

        a_class: the class to check if 'obj' is instance from or
        an instance of a class that inherited from, the specified class

    Return:
        True: True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class

        False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
