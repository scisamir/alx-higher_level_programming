#!/usr/bin/python3
""" Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class inheriting from BaseGeometry Class """
    def __init__(self, width, height):
        """ Init """
        try:
            super().integer_validator("width", width)
            self.__width = width
        except Exception as e:
            raise e

        try:
            super().integer_validator("height", height)
            self.__height = height
        except Exception as e:
            raise e

    def area(self):
        """ Returns area of Rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ Returns str() representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
