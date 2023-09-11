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
