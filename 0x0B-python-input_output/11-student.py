#!/usr/bin/python3
""" Student to disk and reload """


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

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for attr in json:
            if attr in self.__dict__:
                self.__dict__[attr] = json[attr]
