#!/usr/bin/python3
"""

a module containing a matrix_divided function

"""


from hmac import new


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (int) (float): (list of lists) of integers/floats
        div (int) (float): dividend

    Returns:
        int: the sum of 'a' and 'b'

    Raises:
        TypeError: if the type of 'a' or 'b' is not integer/float
    """
    new_matrix = []
    new_list = []

    if type(div) is not int or type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    for i in matrix:
        counter = 0
        if matrix[counter + 1]:
            if len(matrix[counter]) != len(matrix[counter + 1]):
                raise TypeError(
                    "Each row of the matrix must have the same size"
                    )
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
        new_list = []
        counter += 1

    return new_matrix
