#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        fname = cls.__name__ + ".json"
        json_rep = []
        if list_objs is not None:
            for item in list_objs:
                json_rep.append(cls.to_dictionary(item))
        with open(fname, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(json_rep))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            my_instance = cls(1, 1)
        if cls.__name__ == "Square":
            my_instance = cls(1)
        my_instance.update(**dictionary)
        return my_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        fname = cls.__name__ + ".json"
        my_json = []

        try:
            with open(fname, 'r', encoding="utf-8") as f:
                my_json = cls.from_json_string(f.read())
            for key, value in enumerate(my_json):
                my_json[key] = cls.create(**my_json[key])
            return my_json
        except Exception:
            return []
