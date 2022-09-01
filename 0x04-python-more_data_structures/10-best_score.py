#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    val_list = []
    for my_key in a_dictionary:
        val_list.append(a_dictionary[my_key])
    biggest = max(val_list)

    for keyz in a_dictionary:
        if a_dictionary[keyz] == biggest:
            return keyz

