#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    length = len(my_list) - 1
    while length > 0:
        for j in range(length):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
        length -= 1
    return my_list[len(my_list) - 1]
