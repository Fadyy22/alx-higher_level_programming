#!/usr/bin/python3

"""class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    return dict(obj.__dict__)
