#!/usr/bin/python3
"""a module containing class LockedClass """


class LockedClass:
    """
    a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_nam
    """
    __slots__ = ["first_name"]
