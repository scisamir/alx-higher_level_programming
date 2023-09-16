#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ Init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is not None:
            selctd_attrs = {}

            for i in attrs:
                if i in self.__dict__:
                    selctd_attrs[i] = self.__dict__[i]
            return selctd_attrs

        return self.__dict__
