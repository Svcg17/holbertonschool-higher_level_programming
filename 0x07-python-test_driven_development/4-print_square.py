"""4-print_square module"""


def print_square(size):

    """ prints a square with the character #

    Args:
        size: integer that is the size of the square

    Returns:
        prints the square

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
