#!/usr/bin/python3
""" The square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inherited from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """size attribute getter method"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """"assigns attributes to arguments"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.size}
