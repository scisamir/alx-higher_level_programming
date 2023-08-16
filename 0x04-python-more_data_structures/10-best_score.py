#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return
    num = 0
    res = ""
    for a_key in a_dictionary:
        if a_dictionary[a_key] > num:
            num = a_dictionary[a_key]
            res = a_key
    return res
