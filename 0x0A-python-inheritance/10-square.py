#!/usr/bin/python3
""" Square #1 """
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

        super().__init__(size, size)
