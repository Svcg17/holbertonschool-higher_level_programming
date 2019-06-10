#!/usr/bin/python3
import json
""" The base module """


class Base:
    """A Base class

    Attributes:
        __nb_objects: counter for the number of objects in class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
        Args:
            id: memory id of object

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            if type(list_dictionaries) is not list:
                TypeError("list_dictionaries must be a list")
            jsoned = json.dumps(list_dictionaries)
            return jsoned

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs"""
        if list_objs is None:
            to_json_string([])
        else:
            with open(str(cls.__name__) + ".json", mode='w') as f:
                f.to_json_string(list_objs, f)
