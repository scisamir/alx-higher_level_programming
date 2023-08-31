#!/usr/bin/python3
"""
    Define a Class
"""


class Square:
    """
        A class Sqaure that instantates a Square with
        a private attribute, size
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes '__size' to 'size' """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the current square size """

        return self.__size

    @property
    def position(self):
        """ Returns position of the current square """

        return self.__position

    @size.setter
    def size(self, value):
        """ Updates the current square size """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ Updates the current square position """

        isvalid = False

        if isinstance(value, tuple) and len(value) == 2:
            if type(value[0]) == int and type(value[1]) == int:
                if value[0] >= 0 and value[1] >= 0:
                    isvalid = True
        if isvalid:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns the current square area """

        return (self.__size * self.__size)

    def my_print(self):
        """ Prints in stdout the square with the character '#' """

        if (self.__position)[0]:
            sp = " " * (self.__position)[0]
        else:
            sp = ""

        if (self.__position)[1]:
            nwl = "\n" * (self.__position)[1]
        else:
            nwl = "\n"

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print(sp, end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print(nwl, end="")
