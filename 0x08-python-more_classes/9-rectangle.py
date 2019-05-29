#!/usr/bin/python3
""" 9-rectangle module """


class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ class constructor """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    """ getting the width """
    @property
    def width(self):
        return self.__width

    """ setting the width """
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ getting the height """
    @property
    def height(self):
        return self.__height

    """ setting the height """
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mustbe >= 0")
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
        """ prints rectangle """
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += str(self.print_symbol)
            rec += '\n'
        return rec.strip('\n')

    def __repr__(self):
        """ string representation of rectangle """
        temp = ""
        if self.__width == 0 or self.__height == 0:
            return temp
        else:
            temp = ("Rectangle(" + str(self.__width))
            temp += "," + str(self.__height) + ")"
            return temp

    def __del__(self):
        """ deletes an instance """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns biggest rectangle based on an area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
        # return (eval("Rectangle({}, {})".format(size, size)))
