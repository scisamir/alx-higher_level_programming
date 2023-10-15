#!/usr/bin/python3
"""
    Roman to Integer
"""


def roman_to_int(roman_string):
    """ Converts Roman Numeral to Integer """

    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    roman_nines = {"IX": 9, "XC": 90, "CM": 900}
    roman_fours = {"IV": 4, "XL": 40, "CD": 400}
    roman_len = len(roman_string)
    roman_int = 0
    i = 0

    while i < roman_len:
        if i + 1 < roman_len:
            roman_uniq = roman_string[i] + roman_string[i + 1]

            if roman_uniq in roman_nines.keys():
                roman_int += roman_nines[roman_uniq]
                i += 2
                continue
            if roman_uniq in roman_fours.keys():
                roman_int += roman_fours[roman_uniq]
                i += 2
                continue

        roman_int += roman_dict[roman_string[i]]
        i += 1

    return roman_int
