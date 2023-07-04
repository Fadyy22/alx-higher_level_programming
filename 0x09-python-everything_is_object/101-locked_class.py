#!/usr/bin/python3
"""a module containing class LockedClass """


class LockedClass:
    """
    a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_nam
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            error_msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(error_msg)
