#!/usr/bin/python3
""" the 4-append_write module """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file and returns the num of chars
    added.

    Args:
        filename: file to be appended
        text(str): string to be appended

    Returns:
        number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        counter = f.write(text)
        return counter
