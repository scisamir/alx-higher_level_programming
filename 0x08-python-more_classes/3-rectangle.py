#!/usr/bin/python3
"""
    Class Rectangle
"""


class Rectangle:
    """ Class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes width """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the Rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += "#"
                if i != self.__height - 1:
                    rect += "\n"

        return rect
