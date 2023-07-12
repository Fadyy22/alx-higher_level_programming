#!/usr/bin/python3

"""class Student and def to_json(self) function"""


class Student:
    """Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age
    Public method def to_json(self): that retrieves a dictionary representation
    of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            my_dict = {}
            for element in attrs:
                try:
                    my_dict[element] = getattr(self, element)
                except Exception:
                    pass
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for name in json:
            setattr(self, name, json[name])
