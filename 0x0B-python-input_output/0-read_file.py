#!/usr/bin/python3
""" 0-read_file module """


def read_file(filename=""):
    """ function that reads a text file and prints to stdout

    Args:
        filename: file to be read.

    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
