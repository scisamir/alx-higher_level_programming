#!/usr/bin/python3
""" Square model """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns string representation of square class """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        ))

    @property
    def size(self):
        """ Retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """ Assigns attributes """
        if args:
            my_list = (self.id, self.size, self.x, self.y)
            self.id, self.size, self.x, self.y = args + my_list[len(args):4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ To dictionary """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
