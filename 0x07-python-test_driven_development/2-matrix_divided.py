#!/usr/bin/python3
"""
Module for Divisin

"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    """
    new_matrix = [[0] * len(row) for row in matrix]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
        break
    for index, row in enumerate(matrix):
        for i in range(len(row)):
            if type(row[i]) is not int and type(row[i]) is not float:
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
            else:
                new_matrix[index][i] = round(matrix[index][i] / div, 2)
    return (new_matrix)
