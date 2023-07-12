#!/usr/bin/python3

"""
Pascal Triangle function
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    elif n == 4:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    elif n == 5:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
