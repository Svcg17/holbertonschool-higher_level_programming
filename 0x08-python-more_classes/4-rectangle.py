#!/usr/bin/python3
""" 4-rectangle method """


class Rectangle:
    """class constructor

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle


    """
    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getting the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getting the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            c = 0
        else:
            a = self.__height * 2
            b = self.__width * 2
            c = a + b
        return c

    def __str__(self):
        """ print rectangle """
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += '#'
            rec += '\n'
        return rec.strip('\n')

    def __repr__(self):
        """ string representation of the rectangle """
        temp = ""
        a = self.__width
        b = self.__height
        if self.__width == 0 or self.__height == 0:
            return temp
        else:
            temp = ("Rectangle(" + str(a) + "," + str(b) + ")")
            return temp
