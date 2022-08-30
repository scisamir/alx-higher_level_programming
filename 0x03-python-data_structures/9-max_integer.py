#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list) - 1
    while length > 1:
        for j in range(length):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
        length--
    return my_list
