#!/usr/bin/python3
""" the 7-save_to_json_file module """


def save_to_json_file(my_obj, filename):
    """ function that writes an object to a text file, using a
    JSON representation

    Args:
        my_obj: object to be written in file
        filename: file to be written to

    """
    import json
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
