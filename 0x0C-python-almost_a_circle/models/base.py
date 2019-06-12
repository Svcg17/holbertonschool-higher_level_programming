#!/usr/bin/python3
""" The base module
"""
import json
from os import path


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
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            if type(list_dictionaries) is not list:
                raise TypeError("list_dictionaries must be a list")
            jsoned = json.dumps(list_dictionaries)
            return jsoned

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs"""
        newlist = []
        if list_objs is not None:
            for i in list_objs:
                newlist.append(i.to_dictionary())
        with open(cls.__name__ + ".json", mode="w") as f:
            ddict = cls.to_json_string(newlist)
            f.write(ddict)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == "Square":
            dummy2 = cls(2)
            dummy2.update(**dictionary)
            return dummy2

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        lista = []
        if path.isfile(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json") as f:
                hey = cls.from_json_string(f.read())
                for i in hey:
                    lista.append(cls.create(**i))
        return lista
