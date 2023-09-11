#!/usr/bin/python3
""" Square #2 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class inheriting from Rectangle Class """
    def __init__(self, size):
        """ Init """
        try:
            super().integer_validator("size", size)
            self.__size = size
        except Exception as e:
            raise e

    def area(self):
        """ Returns area of Rectangle """
        return (self.__size ** 2)

    def __str__(self):
        """ Returns str() representation of Rectangle """
        return "[Square] {}/{}".format(self.__size, self.__size)
