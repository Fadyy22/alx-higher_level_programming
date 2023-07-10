#!/usr/bin/python3

"""module containing 'MyList' Class"""


class MyList(list):
    """class MyList that inherits 'list' class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        list_cpy = self.copy()
        list_cpy.sort()
        print(list_cpy)
