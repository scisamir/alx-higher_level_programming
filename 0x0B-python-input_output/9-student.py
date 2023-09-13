#!/usr/bin/python3
""" Student to JSON """
import json


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ Init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return json.dumps(self.__dict__)
