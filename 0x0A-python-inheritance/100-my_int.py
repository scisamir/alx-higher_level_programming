#!/usr/bin/python3
""" My integer """


class MyInt(int):
    """ Class MyInt that inherits from int """

    def __eq__(self, value):
        """ overrides equal to """
        return super().__ne__(value)

    def __ne__(self, value):
        """ overrides not equal to """
        return super().__eq__(value)
