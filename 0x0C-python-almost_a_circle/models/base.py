#!/usr/bin/python3
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
