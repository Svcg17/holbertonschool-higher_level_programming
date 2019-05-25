#!/usr/bin/python3
""" add_integer module """
def add_integer(a, b=98):
    """ Function that adds two integers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        a + b

    """
    if a:
        if type(a) == float:
            a = int(a)
        if type(b) == float:
            b = int(b)
        if type(a) != int and type(a) != float:
            raise TypeError("a must be an integer")
        if type(b) != int and type(b) != float:
            raise TypeError("b must be an integer")
        return a + b
    else:
        raise TypeError("a must be an integer")
