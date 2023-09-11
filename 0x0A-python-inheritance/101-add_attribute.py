#!/usr/bin/python3
""" Can I? """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object if it’s possible
        Args:
            obj: the object
            name: the name of the attribute
            value: the value of the attribute
    """

    if (hasattr(obj, '__dict__') or
            (hasattr(type(obj), '__slots__') and name in type(obj).__slots__)):
        setattr(obj, name, value)

    else:
        raise TypeError("can't add new attribute")
