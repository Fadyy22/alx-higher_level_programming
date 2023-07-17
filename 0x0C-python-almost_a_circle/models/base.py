#!/usr/bin/python3

"""module containing the base class 'Base'"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            json_list = []
            if list_objs:
                for i in range(len(list_objs)):
                    json_list.append(list_objs[i].to_dictionary())
            else:
                pass
            f.write(str(cls.to_json_string(json_list)))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(11)

        dummy.update(**dictionary)
        return dummy
