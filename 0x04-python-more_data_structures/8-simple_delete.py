#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for my_key in list(a_dictionary):
        if my_key == key:
            del a_dictionary[key]

