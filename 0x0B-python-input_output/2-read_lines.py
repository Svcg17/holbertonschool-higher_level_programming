#!/usr/bin/python3
""" the 2-read_lines module """


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file and prints it to stdout

    Args:
        filename: file to read from
        nb_lines(int): number of liness to read

    """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for i in f:
            counter += 1
            if nb_lines <= 0 or nb_lines >= counter:
                print(i, end="")
