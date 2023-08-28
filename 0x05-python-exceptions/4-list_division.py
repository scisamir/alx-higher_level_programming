#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    a = 0
    b = 0
    divd = 0

    try:
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                divd = a / b
                new_list.append(divd)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        return (new_list)
