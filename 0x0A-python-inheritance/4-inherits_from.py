#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ Only sub class of """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
