#!/usr/bin/python3

"""module containing 'MyInt' Class"""


class MyInt(int):
    """MyInt class
    MyInt has == and != operators inverted
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
