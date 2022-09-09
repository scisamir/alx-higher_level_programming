#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for my_key in a_dictionary:
        if a_dictionary[my_key] == value:
            to_del = my_key
    del a_dictionary[to_del]
