#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for my_key in list(a_dictionary):
        new_dict[my_key] = a_dictionary[my_key] * 2
    return new_dict

