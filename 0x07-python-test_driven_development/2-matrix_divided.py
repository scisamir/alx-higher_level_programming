#!/usr/bin/python3
"""
    Divide a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    if (isinstance(matrix, list) is False or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if (any(not isinstance(num, int) and not isinstance(num, float)
            for row in matrix for num in row)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    mtx_len = len(matrix[0])

    for i in range(len(matrix)):
        if mtx_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    my_matrix = [[round((num / div), 2) for num in row] for row in matrix]

    return my_matrix
