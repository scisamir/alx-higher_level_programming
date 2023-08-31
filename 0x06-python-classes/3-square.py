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

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the current square area """

        return (self.__size * self.__size)
