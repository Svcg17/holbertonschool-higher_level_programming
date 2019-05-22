#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return size.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not instance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not instance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(num < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        a = self.__size * self.__size
        return a

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for line in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for space in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
