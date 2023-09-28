#!/usr/bin/python3
"""module containing peak() function"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    li = list_of_integers

    if li == []:
        return None

    if li[0] >= li[1]:
        return li[0]
    if li[len(li) - 1] >= li[len(li) - 2]:
        return li[len(li) - 1]

    for i in range(1, len(li) - 1):
        if li[i] >= li[i - 1] and li[i] >= li[i + 1]:
            return li[i]
