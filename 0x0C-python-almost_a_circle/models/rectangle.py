#!/usr/bin/python3
""" The rectangle module"""
from models.base import Base


class Rectangle(Base):
    """ A Rectangle class inherited from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x(int): int value
            y(int): int value
            id: Base class' id attribute

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width

    @property
    def height(self):
        """ height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height

    @property
    def x(self):
        """ x getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(0, self.__y):
            print()
        for row in range(0, self.__height):
            for j in range(0, self.__x):
                print(" ", end="")
            for h in range(0, self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height':
                self.height, 'width': self.width}
