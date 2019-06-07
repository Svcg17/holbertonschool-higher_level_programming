#!/usr/bin/python3
""" the 1-number_of_lines module """


def number_of_lines(filename=""):
    """
    reads n lines of a text file and prints it to stdout
    Args:
        filename: file to count number of lines from

    Return:
        number of lines read

    """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            counter += 1
    return counter
