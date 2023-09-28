#!/usr/bin/python3
"""module containing peak() function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    li = list_of_integers

    if li == []:
        return None
    return max(li)
