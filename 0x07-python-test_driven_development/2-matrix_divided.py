#!/usr/bin/python3
""" matrix_divided module """


def matrix_divided(matrix, div):

    """ Divides all elements of matrix

    Args:
        matrix (list): list of list of integers
        div (int): integer to divide matrix by

    Returns:
        a new list with the divided matrix.

    """
    result = 0
    nuevo = []
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if matrix == [] or matrix == [[]]:
        raise TypeError(error1)
    if type(matrix) != list:
        raise TypeError(error1)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not div:
        raise TypeError("div must be a number")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if matrix and matrix[0]:
        for row in matrix:
            temp = []
            lenirow = matrix[0]
            if len(matrix) != 2:
                raise TypeError(error1)
            if len(row) == 0:
                raise TypeError(error1)
            if len(lenirow) != len(row):
                raise TypeError(error2)
            for j in row:
                if type(j) != int and type(j) != float:
                    raise TypeError(error1)
                result = j / div
                result = round(result, 2)
                temp.append(result)
            nuevo.append(temp)
        return nuevo
    else:
        raise TypeError(error1)
