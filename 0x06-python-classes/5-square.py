#!/usr/bin/python3
"""
    Define a Class
"""


class Square:
    """
        A class Sqaure that instantates a Square with
        a private attribute, size
    """

    def __init__(self, size=0):
        """ Initializes '__size' to 'size' """

        self.size = size

    @property
    def size(self):
        """ Returns the current square size """

        return self.__size

    @size.setter
    def size(self, value):
        """ Updates the current square size """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area """

        return (self.__size * self.__size)

    def my_print(self):
        """ Prints in stdout the square with the character '#' """

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
