#!/usr/bin/python3
""" The square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inherited from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        # PASS SIZE OR WIDTH?
        """returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.__size))

    @property
    def size(self):
        """size attribute getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if size <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = size
        self.__height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """"assigns attributes to arguments"""
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) == 1:
            setattr(self, 'id', args[0])
        elif len(args) == 2:
            setattr(self, 'id', args[0])
            setattr(self, 'size', args[1])
        elif len(args) == 3:
            setattr(self, 'id', args[0])
            setattr(self, 'size', args[1])
            setattr(self, 'x', args[2])
        elif len(args) == 4:
            setattr(self, 'id', args[0])
            setattr(self, 'size', args[1])
            setattr(self, 'x', args[2])
            setattr(self, 'y', args[3])

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
