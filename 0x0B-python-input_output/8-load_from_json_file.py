#!/usr/bin/python3
""" The 8-load_from_json_file module """


def load_from_json_file(filename):
    """ function that creates an Object from a "JSON file"

    Args:
        filename: JSON file to create object from

    """
    import json
    with open(filename, mode='r') as f:
        return json.load(f)
