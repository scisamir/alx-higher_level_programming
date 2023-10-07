#!/usr/bin/python3
"""
    Text indentation
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each
        of these characters: ., ? and :
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    new_text = ""
    i = 0

    while i < len(text):
        if text[i] in ['.', '?', ':']:
            new_text += "\n\n"
            if text[i + 1] == " ":
                i += 1
        else:
            new_text += text[i]
        i += 1

    print(new_text)
