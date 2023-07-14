#!/usr/bin/python3

"""module containing the base class 'Base'"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_nb_objects(cls):
        return cls.__nb_objects

    @classmethod
    def set_nb_objects(cls, value):
        cls.__nb_objects = value
