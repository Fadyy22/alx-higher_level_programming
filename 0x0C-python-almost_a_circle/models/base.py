#!/usr/bin/python3

"""module containing the base class 'Base'"""


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """

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
