#!/usr/bin/python3
""" The 6-from_json_string module """


def from_json_string(my_str):
    """ function that returns an object represented by a JSON string

    Args:
        my_str(str): string to be converted to object

    Returns:
        python object converted, previously a json string

    """
    import json
    jsoned = json.loads(my_str)
    return jsoned
