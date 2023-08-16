#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = sorted(a_dictionary)
    for a_key in dict_keys:
        print("{}: {}".format(a_key, a_dictionary.get(a_key)))
