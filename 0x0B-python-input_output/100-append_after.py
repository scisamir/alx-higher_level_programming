#!/usr/bin/python3
""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line
        containing a specific string
    """
    mod_str = []

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            mod_str.append(line)
            if search_string in line:
                mod_str.append(new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(mod_str)
