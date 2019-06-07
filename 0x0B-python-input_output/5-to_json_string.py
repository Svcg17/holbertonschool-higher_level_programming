#!/usr/bin/python3
""" the 5-to_json_string module """


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object

    Args:
        my_obj: object(str) to be json represented

    Returns:
        json represented my_obj

    """
    import json
    jsoned = json.dumps(my_obj)
    return jsoned
