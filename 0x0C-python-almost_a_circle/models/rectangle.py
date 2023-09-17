#!/usr/bin/python3
""" Rectangle model """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieves x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area """
        return (self.__width * self.__height)

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Returns string representation of the class """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        ))

    def update(self, *args, **kwargs):
        """ Assigns attributes """
        if args:
            my_list = (self.id, self.width, self.height, self.x, self.y)
            self.id, self.width, self.height, self.x, self.y = \
                args + my_list[len(args):5]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ To dictionary """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
