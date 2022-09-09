#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for my_key in sorted_keys:
        print(my_key, end=": ")
        print(a_dictionary[my_key])
