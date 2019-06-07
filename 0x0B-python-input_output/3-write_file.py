#!/usr/bin/python3
""" the 3-write_file module """


def write_file(filename="", text=""):
    """ write a string to a text file and returns the number of characters written

    Args:
        filename: file to write to
        text(str): string to be written inside filename


    Returns:
        number of characters written

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        counter = f.write(text)
        return counter
