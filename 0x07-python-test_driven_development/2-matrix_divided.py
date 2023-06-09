#!/usr/bin/python3
"""

a module containing a matrix_divided function

"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (int) (float): (list of lists) of integers/floats
        div (int) (float): dividend

    Returns:
        matrix: a new matrix (matrix / div)

    Raises:
        TypeError: if matrix is not a list of lists of ints and floats
        TypeError: if rows of the matrix are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is = 0
    """
    new_matrix = []
    new_list = []

    if type(div) is not int or type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(msg_1)

    for i in matrix:
        if type(i) is not list:
            raise TypeError(msg_1)

    for i in matrix:
        counter = 0
        if matrix.index(matrix[counter]) != len(matrix) - 1:
            if len(matrix[counter]) != len(matrix[counter + 1]):
                raise TypeError(msg_2)
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(msg_1)
            new_list.append(round(j / div, 2))
        new_matrix.append(new_list)
        new_list = []
        counter += 1

    return new_matrix
