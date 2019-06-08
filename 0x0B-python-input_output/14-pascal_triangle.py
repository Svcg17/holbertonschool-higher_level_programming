#!/usr/bin/python3
""" The 14-pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal's
    triangle of n

    Args:
        n(int): an integer to be used to represent the triangle
    """
    lista = []
    if (n <= 0):
        return lista

    lista = [[1 for i in range(0, row + 1)] for row in range(0, n)]
    for row in range(1, n):
        for num in range(1, row):
            lista[row][num] = lista[row - 1][num] + lista[row - 1][num - 1]
    return lista
