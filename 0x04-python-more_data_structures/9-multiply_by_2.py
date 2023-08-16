#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_key = a_dictionary.keys()
    return {key_a: a_dictionary[key_a] * 2 for key_a in a_key}
